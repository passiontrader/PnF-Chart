# 📊 NSE Point & Figure (PnF) Chart Generator

![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

A high-density **Point and Figure (PnF)** charting engine for NSE stocks. This tool automates the process of fetching market data, calculating volatility-adjusted price levels, and generating a professional, grid-formatted Excel report with trend predictions.

---

## 🔥 Key Features

* **ATR & Percentage Scaling**: Automatically adjusts box sizes based on stock price and volatility.
* **High-Low Sensitivity**: Uses daily extremes to capture true trend reversals.
* **Automated Signals**: Built-in logic to detect **Double Top Buy** and **Double Bottom Sell** breakouts.
* **Professional Output**: Generates Excel files with a 3.0 "Square-Grid" column width for a classic PnF look.

---

## 🛠️ How to Use (Step-by-Step)

### 1. Install Requirements
You need Python installed. Run this command in your terminal/command prompt to install the necessary libraries:
```bash
pip install yfinance pandas numpy openpyxl
