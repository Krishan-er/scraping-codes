# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:19:07 2021

@author: kgs1
"""
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver = webdriver.Chrome(executable_path='scripts/chromedriver.exe')
driver.get('https://www.zomato.com/chennai/dine-out?rating_range=4.0-5.0')
time.sleep(3)
links = []

first = 'https://www.zomato.com'


soup = bs(driver.page_source, 'lxml')
for link in soup.select('a.sc-ileJJU.brZFmP'):
    data = link.get('href')
    sequence = (first, data)
    finalurl = ''.join(sequence)
    links.append(finalurl)

df = pd.DataFrame({'url': links})
df.to_csv('zomato_chennai_urls.csv', index=False)


