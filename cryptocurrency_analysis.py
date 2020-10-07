# cryptocurrency_analysis.py
# https://jamesgeorgedunn.com/2020/10/05/using-python-and-pandas-to-analyse-cryptocurrencies-with-coinapi/
# 

import json
import requests
import pandas as pd
import datetime as dt

def dt_day_num_to_day_name(number):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    return days[number]

api_key = "API_KEY_HERE"

# "https://rest.coinapi.io/v1/ohlcv/LTC/USD/history?period_id=1DAY&time_start=2015-01-01T00:00:00&time_end=2020-10-31T23:59:00&limit=100000"
url_template = "https://rest.coinapi.io/v1/ohlcv/{}/{}/history?period_id=1DAY&time_start={}T00:00:00&time_end={}T23:59:00&limit={}"

cryptocurrency = "LTC"
price_denomination = "USD"
api_start_date = dt.datetime(2015, 1, 1)
api_end_date = dt.date.today()
print(api_start_date.date, str(api_start_date.strftime("%Y-%m-%d")))
result_limit = 100000
url = url_template.format(cryptocurrency, price_denomination, api_start_date.strftime("%Y-%m-%d"), api_end_date.strftime("%Y-%m-%d"), result_limit)
headers = {"X-CoinAPI-Key": api_key}
response = requests.get(url, headers=headers)

if (response.status_code == 429):
    print("Too many requests. Try again later.")
    
print(response.text)

coin_data = json.loads(response.text)
ltc_data = pd.DataFrame(coin_data)
ltc_data.rename(columns = {
    "time_period_start": "Start Time",
    "time_period_end": "End Time",
    "time_open": "Open Time",
    "time_close": "Close Time",
    "price_open": "Price Open",
    "price_close": "Price Close",
    "price_high": "Price High",
    "price_low": "Price Low",
    "volume_traded": "Volume Traded",
    "trades_count": "Trade Count",
}, inplace = True)
ltc_data.drop(["End Time", "Open Time", "Close Time"], axis = "columns", inplace = True)

reorder_columns = [
    "Start Time",
    "Price Open",
    "Price Close",
    "Price High",
    "Price Low",
    "Volume Traded",
    "Trade Count"
]
ltc_data = ltc_data.reindex(columns = reorder_columns)
ltc_data["Start Time"] = pd.to_datetime(ltc_data["Start Time"])
ltc_data["Day of Week"] = ltc_data["Start Time"].dt.dayofweek
ltc_data["Day of Week"] = ltc_data["Day of Week"].apply(dt_day_num_to_day_name)

# Save data to CSV
ltc_data.to_csv("LTC Day History.csv", index = False)

# Read data from CSV
df = pd.read_csv("LTC Day History.csv")

# Mean of "Price High" column data
print(df["Price High"].describe()["mean"])

# Mean of "Price High" for Sept. 2020
start_date = df["Start Time"] >= "2020-09-01"
end_date = df["Start Time"] <= "2020-09-30"
print(df[start_date & end_date]["Price High"].describe()["mean"])

# Mean of "Price High" for Wednesdays in Sept. 2020
filter_dates = df[start_date & end_date]
print(filter_dates[filter_dates["Day of Week"] == "Wednesday"]["Price High"].describe()["mean"])


