# reddit_python_scraper.py
# https://shrikantpaliwal.com/blog/scraping-reddit-for-questions/

import pandas as pd
import requests
import json
import time
import re

MAX_POSTS = 1000

hdr = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.reddit.com/r/python/.json'

req = requests.get(url, headers=hdr)
json_data = json.loads(req.text)
print(json_data)

data_all = json_data['data']['children']
num_posts = 0
while len(data_all) <= MAX_POSTS:
    print(len(data_all))
    time.sleep(2)
    last = data_all[-1]['data']['name']
    url = 'https://www.reddit.com/r/python/.json?after=' + str(last)
    req = requests.get(url, headers=hdr)
    data = json.loads(req.text)
    data_all += data['data']['children']
    # Break out of loop if no more posts found
    if num_posts == len(data_all):
        break
    else:
        num_posts = len(data_all)
    
print(len(data_all))

# Get "who, what, where, when, why, how" questions
count = 0
df = pd.DataFrame(columns=['questions', 'link_to_answer'])

whPattern = re.compile(r'who|what|how|where|when|why|which|whom|whose', re.IGNORECASE)
for post in data_all:
    whMatch = whPattern.search(str(post['data']['title']))
    if whMatch:
        print(str(post['data']['title']))
        print(str(post['data']['url']))
        count += 1
        # Save to data frame
        df.loc[count] = [str(post['data']['title']), str(post['data']['url'])]
        
# Save data frame to CSV
df.to_csv('reddit_python.csv', sep=',', encoding='utf-8')
