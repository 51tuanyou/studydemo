# agents/email_parser.py
# 从邮件内容解析商品名称
import re

def extract_product_names(email_text: str):
    # 简单用正则匹配商品列表（可以优化）
    pattern = r"(iPhone 15|AirPods Pro|MacBook Pro 16)"
    return re.findall(pattern, email_text)
