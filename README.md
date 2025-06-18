<h1 align="center">CryptoBeat</h1>

<p align="center">
  <a href="https://waveassist.io/assistant/CryptoBeat-Template">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## Overview

Grabs BTC & ETH spot prices from CoinDesk’s BPI endpoint every hour; stores JSON for other nodes and fires an email if either moves > 2 %.

CryptoBeat runs on [WaveAssist](https://waveassist.io), providing lightweight crypto sentiment monitoring without needing a full exchange feed.


---

## One-Click Deploy on WaveAssist (Recommended)

<p>
  <a href="https://waveassist.io/assistant/CryptoBeat-Template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

Deploy CryptoBeat instantly on [WaveAssist](https://waveassist.io).

> 🔐 You may be prompted to log in or create a free WaveAssist account before continuing.

#### How to Use:

1. Click the button above or go to [waveassist.io/assistant/CryptoBeat-Template](https://waveassist.io/assistant/CryptoBeat-Template)
2. Run the starting node:
   - **bitcoin_price_fetcher**: Fetches the current Bitcoin (and Ethereum) prices from CoinDesk’s API.
3. Monitor logs and ensure alerting works as intended.
4. Finally, click **Deploy** to schedule this automation and run it daily.

✅ You’re now monitoring BTC/ETH price shifts on autopilot.

---

## Manual Deployment

Clone this repository and run the following scripts in order:

**Scripts:**

- `bitcoin_price_fetcher.py`
- `btc_price_comparison.py`
- `crypto_price_alert.py`

<details>
<summary>Python Requirements</summary>
  
_No additional Python requirements specified._
</details>

---

## Features

* **BitcoinPriceFetcher**: Pulls the latest BTC (and ETH) prices from CoinDesk’s API.
* **BtcPriceComparison**: Checks the absolute percentage change vs. prior price and computes necessary comparisons.
* **CryptoPriceAlert**: Triggers an email if the movement exceeds 2%.
* **Processing Variables**:
  - `current_prices`
  - `current_price_data`
  - `alert_triggered`
  - `previous_price_data`
  - `price_comparison`

---

Built with ❤️ by the WaveAssist team. Want help or integrations? [Say hello](https://waveassist.io).
