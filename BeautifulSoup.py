# Hyper Text Marker Language (HTML)

import bs4
import requests

# import webbrowser
# webbrowser.open('https://www.amazon.ca/Automate-Boring-Stuff-Python-Programming/dp/1593275994')

headers = {'User-Agent': 'Mozilla 5.0'} # Amazon requires headers
# response = requests.get('https://www.amazon.com', headers=headers)

res = requests.get('https://news.ycombinator.com/', headers=headers)

print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.content, "html.parser")

# s = soup.find('div', class_='entry-content')
# content = s.find_all('p')

# The title tag of the page
print(soup.title)
# Output: <title>Hacker News</title>

# The title of the page as string
print(soup.title.string)
# Output: Hacker News

# All links in the page
nb_links = len(soup.find_all("a"))
print(f"There are {nb_links} links in this page")
# Output: There are 231 links on this page

# Text from the page
print(soup.get_text())
# Output:
# Hacker News
# Hacker News
# new | past | comments | ask | show | jobs | submit
# login
# ...

# def getAmazonPrice(productUrl):
#     headers = {'User-Agent': 'Mozilla 5.0'} # Amazon requires headers
#     res = requests.get(productUrl, headers=headers)
#     res.raise_for_status()

#     soup.select('')

# price = getAmazonPrice('')