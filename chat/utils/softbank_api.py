# utils/softbank_api.py
# 模拟内部商品系统 API
SOFTBANK_PRODUCTS = {
    "iPhone 15": "SB001",
    "AirPods Pro": "SB002",
    "MacBook Pro 16": "SB003",
}

USER_QUOTE_LIMIT = {
    "default": 1000,
    "vip": 2000
}

def find_product_code(name: str):
    return SOFTBANK_PRODUCTS.get(name)

def get_price(product_code: str, user_type: str = "default"):
    base_price = 500  # 模拟基础价格
    limit = USER_QUOTE_LIMIT.get(user_type, 1000)
    return min(base_price + hash(product_code) % 1000, limit)
