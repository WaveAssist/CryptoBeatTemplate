import waveassist
waveassist.init()

# Fetch comparison results
comparison_data = waveassist.fetch_data("price_comparison")

btc_change = comparison_data["btc_change_percent"]
eth_change = comparison_data["eth_change_percent"]

current_price = waveassist.fetch_data("current_price_data")
btc_price = current_price["BTC"]["price"]
eth_price = current_price["ETH"]["price"]
print(f"📌 Current BTC Price: ${btc_price}")
print(f"📌 Current ETH Price: ${eth_price}")

btc_color = "green" if btc_change >= 0 else "red"
btc_sign = "+" if btc_change >= 0 else ""

eth_color = "green" if eth_change >= 0 else "red"
eth_sign = "+" if eth_change >= 0 else ""

html_content = f"""
<div style="font-family: Arial, sans-serif; padding: 12px; border: 1px solid #ffa500; background-color: #ffecb3; border-radius: 6px; max-width: 400px;">
  <p style="margin: 0; font-size: 18px;"><strong>Crypto Price Alert</strong></p>
  <hr style="border: none; border-top: 1px solid #ffa500; margin: 8px 0;">
  <p style="margin: 4px 0;">
    <strong>BTC:</strong> ${btc_price}  
    <span style="color: {btc_color};">
      ({btc_sign}{btc_change:.2f}%)
    </span>
  </p>
  <p style="margin: 4px 0;">
    <strong>ETH:</strong> ${eth_price}  
    <span style="color: {eth_color};">
      ({eth_sign}{eth_change:.2f}%)
    </span>
  </p>
</div>
"""

waveassist.send_email("Your Requested Crypto Price Update!",
    html_content=html_content)
