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
2. Install Dependencies
pip install yfinance pandas numpy openpyxl
3. Run the Generator
python pnf_generator.py
📈 Prediction Logic

The generator doesn't just draw — it thinks. It evaluates the structure of the X and O columns to provide actionable signals:

Signal	Logic	Interpretation
Bullish Breakout	Current 'X' column exceeds the height of the previous 'X' column	Strong Buy (Double Top)
Bearish Breakdown	Current 'O' column falls below the low of the previous 'O' column	Strong Sell (Double Bottom)
Trend Continuation	Price moves within the current column without breakout	Hold Position
📁 Output Structure

When you run the script, it generates a .xlsx file formatted as follows:

Rows 1–10: Metadata
(Scrip Name, Box Size, Current Close, Prediction)
Column A: Price Axis (Descending order)
Grid: The X and O matrix
Footer: Reversal dates for each specific column
🤝 Contributing

Contributions make the open-source community an amazing place to learn and create.

Fork the Project

Create your Feature Branch

git checkout -b feature/AmazingFeature

Commit your Changes

git commit -m "Add AmazingFeature"

Push to the Branch

git push origin feature/AmazingFeature
Open a Pull Request
📜 License

Distributed under the MIT License. See LICENSE for more information.
