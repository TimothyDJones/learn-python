# indeed_job_scraper.py
# https://www.youtube.com/watch?v=eN_3d4JrL_w

import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    """
    Generate the URL using job title/position and location
    """
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)

    return url


def get_record(card):
    """
    Extract details from a job "card" from Indeed.com page.
    """
    atag = card.h2.a
    job_title = atag.get('title')
    job_url = 'https://www.indeed.com' + atag.get('href')

    company = card.find('span', {'class': 'company'}).text.strip()
    job_location = card.find('div', 'recJobLoc').get('data-rc-loc')
    job_summary = card.find('div', 'summary').text.strip()

    post_date = card.find('span', 'date').text
    today = datetime.today().strftime('%Y-%m-%d')

    # If salary range is not provided, set to empty string.
    try:
        job_salary = card.find('span', 'salaryText').text
    except (AttributeError):
        job_salary = ''
    
    record = (job_title, company, job_location, post_date, today, job_summary, job_salary, job_url)

    return record


def main(position, location):
    """
    Main program routine
    """
    records = []
    url = get_url(position, location)
    #url = get_url("it analyst", "Tulsa OK")

    while True:
        response = requests.get(url)
        print(response)

        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'jobsearch-SerpJobCard')

        # Get list of records from each job "card" on page
        for card in cards:
            record = get_record(card)
            records.append(record)

        print(records[0])

        # Handle multiple pages of results
        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')  # Find 'Next' button on page
        except (AttributeError):
            break

    # Save results to CSV file
    output_file = "indeed_jobs_" + datetime.today().strftime('%Y_%m_%d') + ".csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['JobTitle', 'Company', 'Location', 'PostDate', 'ExtractDate', 'Summary', 'Salary', 'JobUrl'])
        writer.writerows(records)

if __name__ == "__main__":
    main("Information Technology", "Tulsa, OK")