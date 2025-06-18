import waveassist
import requests

waveassist.init()

btc_response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
btc_response.raise_for_status()
btc_data = btc_response.json()

eth_response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
eth_response.raise_for_status()
eth_data = eth_response.json()

waveassist.store_data('current_price_data', {
    "BTC": btc_data,
    "ETH": eth_data
})
