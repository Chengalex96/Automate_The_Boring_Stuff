import requests
from bs4 import BeautifulSoup
import time
import json

# Initialize variables
is_scraping = True
current_page = 1
scraped_data = []
max_retries = 3  # Maximum retries for failed requests

print("Hacker News Scraper started...")

# Continue scraping until there are no more pages to scrape
while is_scraping:
    try:
        # Make the request
        response = requests.get(
            f"https://news.ycombinator.com/?p={current_page}")
        html_content = response.content

        print(f"Scraping page {current_page}: {response.url}")

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        articles = soup.find_all(class_="athing")

        if articles:
            # Extract data from each article on the page
            for article in articles:
                article_data = {
                    "URL": article.find(class_="titleline").find("a").get("href"),
                    "title": article.find(class_="titleline").getText(),
                    "rank": article.find(class_="rank").getText().replace(".", ""),
                }
                scraped_data.append(article_data)
            print(f"Page {current_page} scraped successfully, found {len(articles)} articles.")

        # Check if there's a link to the next page
        next_page_link = soup.find(class_="morelink")

        if next_page_link:
            current_page += 1
        else:
            is_scraping = False
            print(f"Finished scraping! Total pages scraped: {current_page}")
            print(f"Total articles scraped: {len(scraped_data)}")

            # Save scraped data to JSON file
            with open("hn_articles.json", "w", encoding="utf-8") as jsonfile:
                json.dump(scraped_data, jsonfile, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scraping page {current_page}: {e}")

        # Implement retry logic with delay (up to max_retries attempts)
        for attempt in range(1, max_retries + 1):
            print(f"Retrying request for page {current_page} (attempt {attempt}/{max_retries})...")
            time.sleep(2)  # Adjust delay as needed
            try:
                response = requests.get(
                    f"https://news.ycombinator.com/?p={current_page}")
                break  # Successful request, exit retry loop
            except requests.exceptions.RequestException:
                pass  # Continue retrying on failure
        else:
            print(f"Giving up after {max_retries} retries for page {current_page}")

    # Always add a delay between requests
    time.sleep(2)