# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:18:16 2021

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
import re
import lxml

list1 = []

with open("swiggy_chennai.csv", mode="w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Name','Address','Reviews','Contact']) 
    
driver = webdriver.Chrome(executable_path='scripts/chromedriver.exe')
driver.get('https://www.swiggy.com/restaurants?sortBy=RATING')
time.sleep(3)

df = pd.read_csv('swiggy_chennai_urls.csv')

for link in df['url'][:200]:
    driver.get(link)
    soup = bs(driver.page_source,'lxml')
    name = soup.find('h1',class_='_3aqeL').getText()
    star = soup.find('div',class_='_2l3H5').getText()
    address = soup.find('div',class_='Gf2NS _2Y6HW').getText()
    reviews = soup.find('span',class_='_1iYuU').getText().replace('ratings','')
         
    print(name)
    list1.append(name)
    list1.append(address)
    list1.append(star)
    list1.append(reviews)
    
    with open("swiggy_chennai.csv", mode="a", newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(list1)
   
    list1 = []


    
    
    
    