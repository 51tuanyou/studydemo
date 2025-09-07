# services/quote_service.py
# 报价服务逻辑
from chat.utils.softbank_api import find_product_code, get_price
import requests

def query_price(product_name: str, user_type: str = "default"):
    code = find_product_code(product_name)
    if code:
        # 内部系统找到
        return get_price(code, user_type)
    else:
        # 外部官网查询（模拟）
        return query_price_from_web(product_name)

def query_price_from_web(product_name: str):
    # 模拟官网 API 请求
    web_prices = {
        "Galaxy S23": 1200,
        "Sony WH-1000XM5": 350
    }
    return web_prices.get(product_name, "Not Found")
