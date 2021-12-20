# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:12:10 2021

@author: kgs1
"""


import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import lxml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import csv


with open("nolen_gur_post1.csv", mode="w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Name','Link','Post'])

option = Options()
data = []

option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


#option.add_argument("--headless")
driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=option)

driver.get('https://www.facebook.com')
mail_id = driver.find_element_by_id('email')
mail_id.send_keys('smartiswarchand@gmail.com')
mail_id.send_keys(Keys.TAB)

password = driver.find_element_by_id('pass')
password.send_keys('kgs18101998')
password.send_keys(Keys.ENTER)


df = pd.read_csv('nolen_gur.csv')

count = 1

for link in df['links']:
    if 'JMRconnect' not in link:
        if 'Deshapriyaparkdurgotsab' not in link:
            driver.get(link)
            data = []
            
            if count == 3:
                break
            
            try:
                name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//h2[@class="gmql0nx0 l94mrbxd p1ri9a11 lzcic4wl aahdfvyu"]')))
                name = name.text
                if name=='Justmyroots':
                    pass
            except Exception:
                print('name exception')
                name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//h5')))
                name = name.text
                
            try:
                see_more = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[contains(text(),"See more")]'))).click()
                
            except Exception:
                print('no see more')
            
            try:
                time.sleep(1)
                post = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="a8nywdso j7796vcc rz4wbd8a l29c1vbm"]')))
                post = post.text
                
            except Exception:
                print('exception')  
                post = 'None'
                
            data.append(name)
            data.append(link)
            data.append(post)
            
            count = count+1
            
            
            with open("nolen_gur_post1.csv", mode="a", newline="", encoding='utf-8') as output_file:
                writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(data)
   
driver.close()

                