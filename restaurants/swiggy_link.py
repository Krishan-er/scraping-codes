# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 12:25:22 2021

@author: kgs1
"""


from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='scripts/chromedriver.exe')
driver.get('https://www.swiggy.com/restaurants?sortBy=RATING')
time.sleep(3)
links = []

location = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@class="_381fS _1oTLG _3BIgv"]')))
#location = driver.find_element_by_xpath('//input[@class="_381fS _1oTLG _3BIgv"]')
location.send_keys('Chennai')
time.sleep(2)
location.send_keys(Keys.DOWN)
location.send_keys(Keys.ENTER)

rating = driver.find_element_by_xpath('//div[contains(text(),"Rating")]').click()
first = 'https://www.swiggy.com'

soup = bs(driver.page_source,'lxml')
for link in soup.find_all('a' , class_='_1j_Yo'):
    data = link.get('href')
    sequence = (first, data)
    finalurl = ''.join(sequence)
    links.append(finalurl)
  

df = pd.DataFrame({'url': links})
df.to_csv('swiggy_chennai_urls.csv', index=False)


