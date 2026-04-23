import json

with open("knowledge.json") as f:
    data = json.load(f)

def get_pricing():
    basic = data["pricing"]["basic"]
    pro = data["pricing"]["pro"]

    return f"""
Basic Plan: {basic['price']}
- {', '.join(basic['features'])}

Pro Plan: {pro['price']}
- {', '.join(pro['features'])}
"""

def get_policy():
    return data["policies"]

