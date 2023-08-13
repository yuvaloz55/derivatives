import yfinance as yf
import pandas as pd

# Define the symbols
symbols = [
    "TSLA", "AAPL", "NVDA", "CCL", "AMZN", "AMD", "SOFI", "MSFT", "MARA", "META",
    "GOOGL", "COIN", "NIO", "RIVN", "NFLX", "F", "PLTR", "NKE", "BAC", "XPEV", "MU",
    "LCID", "JPM", "CVNA", "GOOG", "CMCSA", "BABA", "INTC", "PYPL", "DIS", "RIOT",
    "AI", "ORCL", "SNAP", "SNOW", "DAL", "PFE", "UPST", "RIG", "ATVI", "ENPH", "XOM",
    "OXY", "VZ", "SCHW", "BA", "T", "TGT", "JD", "FCX", "RBLX", "UBER", "ET", "GME",
    "U", "ENVX", "SQ", "SHOP", "C", "WFC", "PLUG", "ADBE", "CHPT", "GM", "AFRM",
    "HOOD", "WBD", "PBR", "ROKU", "AAL", "OSTK", "DKNG", "NCLH", "ABNB", "QCOM", "WMT",
    "UAL", "SBUX", "USB", "PARA", "CRM", "V", "BB"
]


# Initialize an empty list to store the earnings announcement DataFrames
earnings_dataframes = []

# Fetch and store earnings data for each symbol
for symbol in symbols:
    try:
        # Fetch earnings data for the specified symbol
        stock = yf.Ticker(symbol)
        earnings_dates = stock.get_earnings_dates(limit=20)
        # Add the 'Symbol' column
        earnings_dates['Symbol'] = symbol
        # Append the earnings announcement dates DataFrame to the list
        earnings_dataframes.append(earnings_dates)
    except Exception as e:
        print(f"Error fetching earnings data for {symbol}: {str(e)}")

# Combine the earnings announcement DataFrames into a single DataFrame
all_earnings_dates = pd.concat(earnings_dataframes, ignore_index=False)
all_earnings_dates = all_earnings_dates.reset_index()
# Convert the 'Earnings Date' column to timezone-unaware datetimes
all_earnings_dates['Earnings Date'] = all_earnings_dates['Earnings Date'].dt.tz_localize(None)
# print(all_earnings_dates)

# Export the combined earnings announcement dates to an Excel file
excel_filename = "earnings_dates_v4.xlsx"
all_earnings_dates.to_excel(excel_filename, index=False)

