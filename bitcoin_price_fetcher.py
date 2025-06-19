import waveassist
import requests

waveassist.init()

btc_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd')
btc_response.raise_for_status()
prices = btc_response.json()

waveassist.store_data('current_price_data', {
    "BTC": {"price": prices["bitcoin"]["usd"]},
    "ETH": {"price": prices["ethereum"]["usd"]}
})
