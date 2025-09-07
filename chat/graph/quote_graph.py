# graph/quote_graph.py
from langgraph.graph import StateGraph, END
from chat.agents.email_parser import extract_product_names
from chat.services.quote_service import query_price_from_web, get_price, find_product_code


# 定义 State（LangGraph 的状态会在节点间传递）
class QuoteState(dict):
    """State container for quote graph.
    Keys will be merged/updated as the workflow progresses.
    """
    pass


# Node: 从邮件文本提取商品
def parse_email_node(state: QuoteState):
    product_names = extract_product_names(state["input_text"])
    state["product_names"] = product_names
    return state


# Node: 查询内部系统报价
def internal_price_node(state: QuoteState):
    product_names = state.get("product_names", [])
    user_type = state.get("user_type", "default")

    result = {}
    for name in product_names:
        code = find_product_code(name)
        if code:
            price = get_price(code, user_type)
            result[name] = {"price": price, "source": "internal"}
        else:
            result[name] = None  # 内部找不到
    state["internal_result"] = result
    return state


# Node: 查询外部官网报价
def external_price_node(state: QuoteState):
    internal_result = state.get("internal_result", {})
    result = {}
    for name, info in internal_result.items():
        if info is None:
            price = query_price_from_web(name)
            result[name] = {"price": price, "source": "web"}
        else:
            result[name] = info
    state["final_result"] = result
    return state


# 构建 StateGraph
graph = StateGraph(QuoteState)

graph.add_node("ParseEmail", parse_email_node)
graph.add_node("InternalPrice", internal_price_node)
graph.add_node("ExternalPrice", external_price_node)

# 设置执行流程
graph.set_entry_point("ParseEmail")
graph.add_edge("ParseEmail", "InternalPrice")
graph.add_edge("InternalPrice", "ExternalPrice")
graph.add_edge("ExternalPrice", END)

# 编译 workflow
quote_graph = graph.compile()


# Example usage
if __name__ == "__main__":
    email_text = "Hello, I want the price of iPhone 15 and Galaxy S23."
    state = {"input_text": email_text, "user_type": "default"}
    result = quote_graph.invoke(state)
    print(result["final_result"])
