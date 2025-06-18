import waveassist
waveassist.init()

# Fetch comparison results
comparison_data = waveassist.fetch_data("price_comparison")

btc_change = comparison_data["btc_change_percent"]
eth_change = comparison_data["eth_change_percent"]

should_send_email = abs(btc_change) > 0.5 or abs(eth_change) > 0.5


current_price = waveassist.fetch_data("current_price_data")
btc_price = current_price["BTC"]["price"]
eth_price = current_price["ETH"]["price"]

message = f"""
⚠️ Crypto Price Alert:

BTC Price: ${btc_price} | Change: {btc_change:.2f}%
ETH Price: ${eth_price} | Change: {eth_change:.2f}%
"""

waveassist.send_email("Crypto Price Alert 🚨", message.strip())
