# handlers/quote_handler.py
# 处理请求
from chat.agents.email_parser import extract_product_names
from chat.services.quote_service import query_price

def handle_email_quote(email_text: str, user_type: str = "default"):
    product_names = extract_product_names(email_text)
    result = {}
    for name in product_names:
        price = query_price(name, user_type)
        result[name] = price
    return result
