# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:39:24 2021

@author: kgs1
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions
from bs4 import BeautifulSoup as bs
import lxml

link_linkedin = []
scroll_pause_time= 0.6
chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
driver.get("https://www.linkedin.com/search/results/content/?keywords=justmyroots&origin=GLOBAL_SEARCH_HEADER&sid=jtm")

sign_in=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Sign in'))).click()

user_name=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'username')))
user_name.clear()
user_name.send_keys('smartiswarchand@gmail.com')

password=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'password')))
password.clear()
password.send_keys('kgs18101998',Keys.ENTER)

divs = driver.find_elements_by_xpath('//div[@class="mh4"]')
for div in divs:
    div.click()    
    try:
        send = driver.find_element_by_css_selector("div.send-privately-button > button")
        driver.execute_script("arguments[0].click();", send)
        link = driver.find_element_by_xpath('(//div[@class="msg-form__msg-content-container--scrollable scrollable relative"]//a[@class="tap-target feed-shared-mini-update-v2__link-to-details-page text-body-medium ember-view"])[1]').get_attribute('href')
        link_linkedin.append(link)
        driver.find_element_by_xpath('//button[@data-control-name="overlay.close_conversation_window"]').click()
    except Exception:
        continue

        
for page_count in range(2, 8):
    page_count = str(page_count)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'search-marvel-srp-scroll-container')))
    driver.execute_script("return arguments[0].scrollTop = arguments[0].scrollHeight",element)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@aria-label='Page "+page_count+"']"))).click()
    time.sleep(2)
    divs = driver.find_elements_by_xpath('//div[@class="mh4"]')
    for div in divs:
        div.click()    
        try:
            send = driver.find_element_by_css_selector("div.send-privately-button > button")
            driver.execute_script("arguments[0].click();", send)
            link = driver.find_element_by_xpath('(//div[@class="msg-form__msg-content-container--scrollable scrollable relative"]//a[@class="tap-target feed-shared-mini-update-v2__link-to-details-page text-body-medium ember-view"])[1]').get_attribute('href')
            link_linkedin.append(link)
            driver.find_element_by_xpath('//button[@data-control-name="overlay.close_conversation_window"]').click()
        except Exception:
            continue
    
    

df = pd.DataFrame({'Links': link_linkedin})
df.to_csv('linkedIn_jmr_8_10.csv', index=False)  
    
    