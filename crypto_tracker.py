import requests
import pandas as pd
from datetime import datetime
import os

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# API parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": "false"
}

# Get crypto data
response = requests.get(url, params=params)
data = response.json()

# Store crypto data
crypto_data = []

# Current date and time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Extract required data
for coin in data:
    crypto_data.append({
        "Date & Time": current_time,
        "Name": coin["name"],
        "Symbol": coin["symbol"].upper(),
        "Price (USD)": coin["current_price"],
        "Market Cap": coin["market_cap"],
        "24h Change (%)": coin["price_change_percentage_24h"]
    })

# Create DataFrame
new_df = pd.DataFrame(crypto_data)

# CSV file
file_name = "crypto_prices.csv"

# Add new data to historical data
if os.path.exists(file_name):
    old_df = pd.read_csv(file_name)
    final_df = pd.concat([old_df, new_df], ignore_index=True)
else:
    final_df = new_df

# Save historical data
final_df.to_csv(file_name, index=False)

print("Historical crypto data saved successfully!")

# Show only latest 10 records
latest_data = final_df.tail(10)

print("\nLatest 10 crypto records:")
print(latest_data)

# Ask minimum price
min_price = float(input("\nEnter minimum price in USD: "))

# Filter crypto by price
filtered_df = final_df[
    final_df["Price (USD)"] >= min_price
]

print("\nCryptocurrencies above the selected price:")
print(filtered_df)

# Sort from highest price to lowest
sorted_df = filtered_df.sort_values(
    by="Price (USD)",
    ascending=False
)

print("\nSorted cryptocurrencies by price:")
print(sorted_df)

# Count filtered records
print("\nTotal cryptocurrencies found:", len(sorted_df))