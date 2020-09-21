# Display a random quote from REST API

import json
# import urllib2
import requests

# See http://forismatic.com/en/api/ for API details.
url = "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"

# data = json.load(urllib2.urlopen(url))
response = requests.get(url)

print(response.status_code)
print(response.headers)
if (response.status_code == 200):
	print(response.json())
	author = ""
	if response.json()['quoteAuthor'].strip() == "":
		author = "Unknown"
	else:
		author = response.json()['quoteAuthor'].strip()

	print("\n\t" + response.json()['quoteText'].strip() + " —" + author + "\n")
