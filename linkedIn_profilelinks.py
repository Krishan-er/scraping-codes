# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 12:37:13 2021

@author: kgs1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
import lxml

link_linkedin = []
scroll_pause_time= 0.6
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get("https://www.linkedin.com/search/results/content/?keywords=justmyroots&origin=GLOBAL_SEARCH_HEADER&sid=jtm")

sign_in=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Sign in'))).click()

user_name=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'username')))
user_name.clear()
user_name.send_keys('mail')

password=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'password')))
password.clear()
password.send_keys('pass',Keys.ENTER)


soup = bs(driver.page_source,'lxml')
links = soup.select('span>a.app-aware-link')
for i in links:
    link = i.get('href')
    link_linkedin.append(link)
    
        
for page_count in range(2, 22):
    page_count = str(page_count)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'search-marvel-srp-scroll-container')))
    driver.execute_script("return arguments[0].scrollTop = arguments[0].scrollHeight",element)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Page "+page_count+"']"))).click()
    time.sleep(2)
    soup = bs(driver.page_source,'lxml')
    links = soup.select('span>a.app-aware-link')
    for i in links:
        link = i.get('href')
        link_linkedin.append(link)
    
flist = list(set(link_linkedin))
df = pd.DataFrame({'Links': flist})
df.to_csv('linkedIn_jmr.csv', index=False)

        
    
