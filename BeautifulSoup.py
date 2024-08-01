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


def getTemp(productUrl):
    headers = {'User-Agent': 'Mozilla 5.0'} # Amazon requires headers
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#current_conditions-summary > p.myforecast-current-lrg')

    return elems[0].text.strip()

temp = getTemp('https://forecast.weather.gov/MapClick.php?lat=36.37410569300005&lon=-119.27022999999997')
print('The temperature is ' + temp)