import waveassist
import requests

waveassist.init()

# Fetch current price data
current_data = waveassist.fetch_data("current_price_data")
print("Current Price Data:", current_data)

# If current_data is None, fetch from Binance API
if current_data is None:
    btc = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()
    eth = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT').json()
    current_data = {
        "BTC": {"price": float(btc["price"])},
        "ETH": {"price": float(eth["price"])}
    }
    # Store the fetched data
    waveassist.store_data("current_price_data", current_data)

# Get current prices
current_btc = float(current_data["BTC"]["price"])
current_eth = float(current_data["ETH"]["price"])

print("Current BTC Price:", current_btc)
print("Current ETH Price:", current_eth)

# Try to fetch previous price data
# Fetch previous data safely
previous_data = waveassist.fetch_data("previous_price_data")

if previous_data:
    has_previous = True
else:
    has_previous = False
    btc = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd').json()
    eth = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd').json()
    previous_data = {
        "BTC": {"price": btc["bitcoin"]["usd"]},
        "ETH": {"price": eth["ethereum"]["usd"]}
    }

# Extract prices
previous_btc = float(previous_data["BTC"]["price"])
previous_eth = float(previous_data["ETH"]["price"])

# Compare
btc_change_percent = ((current_btc - previous_btc) / previous_btc * 100) if previous_btc else 0
eth_change_percent = ((current_eth - previous_eth) / previous_eth * 100) if previous_eth else 0

print("Previous BTC Price:", previous_btc)
print("BTC Change Percent:", btc_change_percent)
print("ETH Change Percent:", eth_change_percent)

# Store results
waveassist.store_data("price_comparison", {
    "btc_change_percent": btc_change_percent,
    "eth_change_percent": eth_change_percent,
    "has_previous": has_previous
})
waveassist.store_data("previous_price_data", current_data)