# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:52:19 2021

@author: kgs1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup as bs

city = 'mumbai'
sleep_time= randint(1, 3)
data = []
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(f'https://www.google.com/maps/search/mango+farms+in+{city}/@12.9671724,77.5257102,11z/data=!3m1!4b1')
    
while True:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//div[@aria-label="Results for mango farms in mumbai"]')))
    
    for i in range(5):
        driver.execute_script("return arguments[0].scrollTop = arguments[0].scrollHeight",element) 
        time.sleep(sleep_time)
    
    soup = bs(driver.page_source,'lxml')
    
    links = soup.find_all('a',class_='a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
    
    for link in links:
        hp = link['href']
        # print(hp)
        data.append(hp)
        
    try:
        next = driver.find_element_by_xpath('(//img[@class="hV1iCc-icon"])[2]')
        next.click()
        
    except Exception:
        break
    
df = pd.DataFrame({'link':data})
df.to_csv(f'{city}.csv',index = False)
    
driver.close()
    
    
    
    
    
    
    