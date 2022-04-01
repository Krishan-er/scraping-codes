# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 09:41:29 2022

@author: kgs1
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import csv

chrome_options = Options()
city = 'mumbai farms'

# with open(f"{city} maps.csv", mode="w", newline="", encoding='utf-8') as output_file:
#     writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
#     writer.writerow(['Name','Address','Mobile','Website','Link']) 
   
data = []
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver=webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
driver.get('https://www.google.com/maps/search/hostel+in+Ahmedabad,+Gujarat/@23.0258305,72.5427046,17z/data=!3m1!4b1')

df = pd.read_csv('mumbai.csv')

for item in df['link']:
    time.sleep(1)
    try:
        driver.get(item)
    except Exception:
        print('URL not Working')
        continue
    time.sleep(1)
    soup = bs(driver.page_source,'lxml')
    name = soup.find('h1').getText()
    
    try:
        # reviews = int(soup.find('span',class_="OAO0-ZEhYpd-vJ7A6b OAO0-ZEhYpd-vJ7A6b-qnnXGd").getText().replace('reviews','').replace('review',''))
        address = soup.find_all('div',class_="rogA2c")[0].getText()
        # if reviews < 40:
        #     continue
    except Exception:
        address = ''
        
    try:
        mobile_no = soup.find('button',{"data-tooltip":"Copy phone number"}).getText()
    except Exception:
        mobile_no = ''
        try:
            website = soup.find('button',{"data-tooltip":"Open website"}).getText()
        except Exception:
            continue
            
    try:
        website = soup.find('button',{"data-tooltip":"Open website"}).getText()
    except Exception:
        website = ''
        
    data.append(name)
    data.append(address)
    data.append(mobile_no)
    data.append(website)
    data.append(item)
    data = [str(x).replace("\n", ' ').replace("\t", '').replace("\r", '').strip() if x else '' for x in data]
    print(data)
    
    with open(f"{city} maps.csv", mode="a", newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(data)
    
    data = []