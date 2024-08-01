from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://automatetheboringstuff.com/')

elem = browser.find_element(By.CSS_SELECTOR,'.main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(1) > a:nth-child(1)')
elem.click()

elem = browser.find_elements(By.CSS_SELECTOR,'p')
print(len(elem))

# Can input search fields, forward, back, quit

elem = browser.find_element(By.CSS_SELECTOR, 'html')

print(elem.text)