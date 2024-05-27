import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website(url, output_format='csv'):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract data from HTML
    data_list = []
    # Example: scraping headlines from a news website
    headlines = soup.find_all('h2', class_='headline')
    for headline in headlines:
        data_list.append(headline.text.strip())

    # Write data to CSV or JSON
    if output_format == 'csv':
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Headline'])
            for data in data_list:
                writer.writerow([data])
        print("Data has been saved to output.csv")
    elif output_format == 'json':
        with open('output.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data_list, jsonfile, ensure_ascii=False, indent=4)
        print("Data has been saved to output.json")