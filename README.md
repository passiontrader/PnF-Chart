# NSE Point & Figure (PnF) Chart Generator

A professional-grade Python tool designed to generate high-density Point and Figure (PnF) charts for National Stock Exchange (NSE) stocks. This tool fetches real-time data, calculates volatility-adjusted box sizes, and exports a perfectly formatted "square-grid" Excel chart complete with trend predictions and breakout signals.

## ✨ Features

-   **Dynamic Data Fetching:** Integrates with `yfinance` to pull the latest daily High-Low-Close data for any NSE ticker.
    
-   **Volatility-Based Scaling:** Uses **Average True Range (ATR)** or **Percentage-based** logic to define box sizes, ensuring the chart scales correctly to the stock's specific price and volatility.
    
-   **High-Density Plotting:** Optimized to produce detailed charts (similar to professional platforms like Dhelm) by using granular price levels.
    
-   **Professional Excel Output:** * **Square-Grid Look:** Automatically adjusts Excel column widths to create a compact, readable PnF grid.
    
    -   **Metadata Header:** Includes Scrip name, Box size, Reversal settings, and current Close price.
        
    -   **Timeline:** Dates are automatically mapped to the bottom of each column for easy historical reference.
        
-   **Advanced Prediction Logic:** * **Trend Identification:** Labels current sentiment as Bullish (X) or Bearish (O).
    
    -   **Breakout Signals:** Identifies **Double Top Buy** and **Double Bottom Sell** signals by comparing current price action against previous columns.
        

## 🛠️ How It Works

### 1. The PnF Logic

The script uses the standard **3-Box Reversal** method. It employs the **High-Low method** for price updates, which is more sensitive to intraday volatility than the "Close" method, making it superior for identifying true trend reversals.

### 2. Trend Prediction

-   **Double Top Buy:** Triggered when a column of 'X' exceeds the height of the previous 'X' column.
    
-   **Double Bottom Sell:** Triggered when a column of 'O' falls below the low of the previous 'O' column.
    

![](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcQJahE1vdJRZgThJIIeHBDzkBAT8URvksOdqfmmo4c_JIc6lLIiwWUEHUjfYKrg0gqgAsOneB3G9Muya_9FEzX1EraagvBGFsFtrKZat3B2GpYRaXM)

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed, then install the necessary dependencies:

Bash

```
pip install yfinance pandas numpy openpyxl

```

### Installation

1.  Clone the repository:
    
    Bash
    
    ```
    git clone https://github.com/passiontrader/PnF-Chart.git
    
    ```
    
2.  Run the script:
    
    Bash
    
    ```
    python pnf_generator.py
    
    ```
    
3.  Enter the NSE symbol when prompted (e.g., `HDFCBANK` or `SBIN`).
    

## 📊 Sample Output

The generated Excel file will contain:

1.  **Summary Header:** Stock info and the current Buy/Sell signal.
    
2.  **PnF Grid:** A visual map of X's and O's with a price axis on the left.
    
3.  **Dates:** The exact date each column began.
    

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
