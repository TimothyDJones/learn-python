# yahoo_finance_scraper.py
# https://www.youtube.com/watch?v=fw4gK-leExw

import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests

url_stats = "https://finance.yahoo.com/quote/{}/key-statistics?p={}"
url_profile = "https://finance.yahoo.com/quote/{}/profile?p={}"
url_financials = "https://finance.yahoo.com/quote/{}/financials?p={}"

stock = "CTL"

headers = {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    "Dnt": "1", 
    "Host": "finance.yahoo.com", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent":"User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}
response = requests.get(url_financials.format(stock, stock), headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

pattern = re.compile(r"\s--\sData\s--\s")
script_data = soup.find('script', text=pattern).contents[0]
print(script_data[500:])
print(script_data[:500])
start = script_data.find("context") - 2     # Start of actual data in the JavaScript function
json_data = json.loads(script_data[start:-12])
print(json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"].keys())

annual_is = json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["incomeStatementHistory"]["incomeStatementHistory"]
quarterly_is = json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["incomeStatementHistoryQuarterly"]["incomeStatementHistory"]

annual_cf = json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["cashflowStatementHistory"]["cashflowStatements"]
quarterly_cf = json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["cashflowStatementHistoryQuarterly"]["cashflowStatements"]

annual_bs = json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["balanceSheetHistory"]["balanceSheetStatements"]
quarterly_bs = json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["balanceSheetHistoryQuarterly"]["balanceSheetStatements"]

print(annual_is[0])

annual_is_stats = []
for s in annual_is:
    statement = {}
    for key, val in s.items():
        try:
            statement[key] = val["raw"]
        except (TypeError, KeyError):   # Skip empty/missing values
            continue
    annual_is_stats.append(statement)

print(annual_is_stats[0])

# Profile Data
response = requests.get(url_profile.format(stock, stock), headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
pattern = re.compile(r"\s--\sData\s--\s")
script_data = soup.find('script', text=pattern).contents[0]
start = script_data.find("context") - 2     # Start of actual data in the JavaScript function
json_data = json.loads(script_data[start:-12])
print(json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"].keys())
print(json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["assetProfile"])
json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["assetProfile"]["companyOfficers"]
json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["assetProfile"]["longBusinessSummary"]

# Statistics 
response = requests.get(url_stats.format(stock, stock), headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
pattern = re.compile(r"\s--\sData\s--\s")
script_data = soup.find('script', text=pattern).contents[0]
start = script_data.find("context") - 2     # Start of actual data in the JavaScript function
json_data = json.loads(script_data[start:-12])
print(json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"].keys())
print(json_data["context"]["dispatcher"]["stores"]["QuoteSummaryStore"]["defaultKeyStatistics"])

# Historical Stock Data
stock_url = "https://query1.finance.yahoo.com/v7/finance/download/{}"

params = {
    # period1: 1569186357,
    #period2: 1600808757,
    "range": "5y",
    "interval": "1d",
    "events": "history"
}

response = requests.get(stock_url.format(stock), params=params)
file = StringIO(response.text)
reader = csv.reader(file)
data = list(reader)
for row in data[:5]:
    print(row)
