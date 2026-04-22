import yfinance as yf
import pandas as pd
import numpy as np
import os
from datetime import datetime

def generate_pnf_analysis(ticker_input):
    symbol = ticker_input.upper()
    if not symbol.endswith(".NS"):
        symbol += ".NS"
    
    print(f"--- Downloading Data for {symbol} ---")
    df = yf.download(symbol, period="1y", interval="1d")
    if df.empty:
        print("No data found.")
        return

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 1. Box Size Logic (0.5% for high density)
    current_price = float(df['Close'].iloc[-1])
    box_size = round(current_price * 0.005, 2) 
    reversal_limit = 3 

    # 2. PNF Logic (High-Low Method)
    highs, lows = df['High'].values.flatten(), df['Low'].values.flatten()
    dates = df.index.tolist()
    columns, current_col, mode, col_start_date = [], [], None, None
    
    last_h, last_l = float(highs[0]), float(lows[0])
    for i in range(1, len(highs)):
        h, l = float(highs[i]), float(lows[i])
        if h >= last_h + box_size:
            mode = 'X'; col_start_date = dates[i]
            current_col = [last_h + (j * box_size) for j in range(1, int((h - last_h)//box_size) + 1)]
            last_idx = i; break
        elif l <= last_l - box_size:
            mode = 'O'; col_start_date = dates[i]
            current_col = [last_l - (j * box_size) for j in range(1, int((last_l - l)//box_size) + 1)]
            last_idx = i; break
    
    for i in range(last_idx + 1, len(highs)):
        h, l = float(highs[i]), float(lows[i])
        if mode == 'X':
            if h >= max(current_col) + box_size:
                steps = int((h - max(current_col)) // box_size)
                for _ in range(steps): current_col.append(max(current_col) + box_size)
            elif l <= max(current_col) - (box_size * reversal_limit):
                columns.append({'type': 'X', 'data': current_col, 'date': col_start_date})
                mode = 'O'; col_start_date = dates[i]
                steps = int((max(current_col) - l) // box_size)
                current_col = [max(current_col) - (j * box_size) for j in range(1, steps + 1)]
        elif mode == 'O':
            if l <= min(current_col) - box_size:
                steps = int((min(current_col) - l) // box_size)
                for _ in range(steps): current_col.append(min(current_col) - box_size)
            elif h >= min(current_col) + (box_size * reversal_limit):
                columns.append({'type': 'O', 'data': current_col, 'date': col_start_date})
                mode = 'X'; col_start_date = dates[i]
                steps = int((h - min(current_col)) // box_size)
                current_col = [min(current_col) + (j * box_size) for j in range(1, steps + 1)]
    
    if current_col: columns.append({'type': mode, 'data': current_col, 'date': col_start_date})
    
    # --- PREDICTION LOGIC ---
    last_col = columns[-1]
    prediction = "Bullish" if last_col['type'] == 'X' else "Bearish"
    signal = "Neutral"
    
    # Check for Double Top Buy or Double Bottom Sell
    if len(columns) >= 3:
        prev_same_type = columns[-3] # The previous X or O column
        if last_col['type'] == 'X' and max(last_col['data']) > max(prev_same_type['data']):
            signal = "Double Top Buy (Breakout)"
        elif last_col['type'] == 'O' and min(last_col['data']) < min(prev_same_type['data']):
            signal = "Double Bottom Sell (Breakdown)"

    # 3. Trend & Excel Prep
    filename = f"{ticker_input.upper()}_PnF.xlsx"
    all_p = [v for c in columns for v in c['data']]
    y_axis = sorted(list(set([round(float(v), 2) for v in all_p])), reverse=True)
    
    meta = [
        [f"Exchange : NSE || Scrip : {ticker_input.upper()}"], [""],
        [f"Type : highlow || Date : {datetime.now().strftime('%Y-%m-%d')}"], [""],
        [f"Box : {box_size} || Close : {round(current_price, 2)}"], [""],
        [f"Reversal : {reversal_limit}"], [""],
        [f"PREDICTION : {prediction} || SIGNAL : {signal}"], # <--- ADD THIS LINE
        [""], [""]
    ]
    
    grid = []
    for p in y_axis:
        row = [p]
        for col in columns:
            row.append(col['type'] if any(abs(v - p) < (box_size/2) for v in col['data']) else "")
        grid.append(row)
    
    final_sheet = meta + grid + [[""], ["Date"] + [c['date'].strftime('%Y-%m-%d') for c in columns]]
    
    # 4. EXCEL FORMATTING (The "Thin Column" Fix)
    df_out = pd.DataFrame(final_sheet)
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        df_out.to_excel(writer, index=False, header=False, sheet_name='PnF Chart')
        
        workbook = writer.book
        worksheet = writer.sheets['PnF Chart']
        
        # Set Column A (Prices) to be wider
        worksheet.column_dimensions['A'].width = 12
        
        # Set all other columns (B onwards) to be thin for X and O
        from openpyxl.utils import get_column_letter
        for col_idx in range(2, len(columns) + 2):
            col_letter = get_column_letter(col_idx)
            worksheet.column_dimensions[col_letter].width = 3.0 # Accommodates one character
            
    print(f"Success! Square-grid chart saved: {os.path.abspath(filename)}")
    input("Press Enter to exit ...")

if __name__ == "__main__":
    ticker = input("Enter NSE Stock (e.g., SBIN): ")
    generate_pnf_analysis(ticker)
