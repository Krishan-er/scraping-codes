# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:46:28 2021

@author: kgs1
"""

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import csv
import lxml

list1 = []

with open("zomato_chennai.csv", mode="w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Name','Address','Reviews','Contact']) 
    
driver = webdriver.Chrome(executable_path='scripts/chromedriver.exe')
driver.get('https://www.zomato.com/chennai/dine-out?rating_range=4.0-5.0')
time.sleep(3)

df = pd.read_csv('zomato_chennai_urls.csv')

for link in df['url']:
    driver.get(link)
    time.sleep(3)
    reviews = driver.find_element_by_xpath('(//div[@class="sc-1q7bklc-8 kEgyiI"])[1]')
    reviews = reviews.text
    soup = bs(driver.page_source,'lxml')
    title = soup.find('h1', class_="sc-7kepeu-0 sc-iqzUVk curLQu").getText()
    address = soup.find('p', class_="sc-1hez2tp-0 clKRrC").getText()
    contact = soup.find('p', class_="sc-1hez2tp-0 fanwIZ").getText()
    list1.append(title)
    list1.append(address)
    list1.append(reviews)
    list1.append(contact)
    print(list1)
    with open("zomato_chennai.csv", mode="a", newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(list1)
    list1 = []











