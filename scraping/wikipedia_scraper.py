# wikipedia_scraper.py
# https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/

import requests
import random
from bs4 import BeautifulSoup

def scrape_wiki_article(url):
    response = requests.get(url=url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    #title = soup.find(id="firstHeading")
    title = soup.find(id="section_0")
    print(title.text)
    
    all_links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(all_links)
    link_to_scrape = 0
    
    for link in all_links:
        # Skip link if not to other Wikipedia article.
        if link["href"].find("/wiki/") == -1:
            continue
        
        link_to_scrape = link
        break
        
    scrape_wiki_article("https://en.m.wikipedia.org" + link_to_scrape["href"])

if __name__ == "__main__":
    scrape_wiki_article("https://en.m.wikipedia.org/wiki/Web_scraping")
