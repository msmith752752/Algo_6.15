import alpaca_trade_api as tradeapi

# === Replace with your actual paper trading API keys ===
API_KEY = 'PKYQ5NPXTOM2QY0YXDBN'
SECRET_KEY = 'zFWNNRks4OWABPNgJRDSWgZ8AOypuDvROvvbtUI0'
BASE_URL = 'https://paper-api.alpaca.markets/'

from alpaca_trade_api import REST

# === Connect to Alpaca ===
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# === Order details ===
symbol = 'JEPI'
qty = 36
side = 'buy'
order_type = 'limit'
time_in_force = 'gtc'
limit_price = 56.35

try:
    # === Submit the order ===
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=order_type,
        time_in_force=time_in_force,
        limit_price=limit_price
    )
    print(f"✅ Order submitted: {order.id}")

except Exception as e:
    print("❌ Order failed:", e)