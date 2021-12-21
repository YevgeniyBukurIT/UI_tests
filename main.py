import time
from selenium import webdriver
from selenium.webdriver import Keys

browser = webdriver.Chrome("chromedriver/chromedriver.exe")
browser.get("https://www.foxtrot.com.ua/uk")

browser.implicitly_wait(30)

search = 'Телевізор'
h1 = 'Телевізори'

browser.find_element_by_css_selector('[type="search"]').send_keys(search)
browser.find_element_by_css_selector('[type="search"]').send_keys(Keys.RETURN)

actual_text = browser.find_element_by_css_selector('h1.with-counter').text

expected_text = h1

print(actual_text == expected_text)

assert actual_text == expected_text
