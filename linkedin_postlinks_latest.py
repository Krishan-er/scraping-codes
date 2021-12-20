# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:19:58 2021

@author: kgs1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from random import randint
from selenium.webdriver.chrome.options import Options
import selenium.common.exceptions
from bs4 import BeautifulSoup as bs
import lxml

link_linkedin = []
num = randint(3, 6)
#scroll_pause_time= 0.6
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver=webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
driver.get("https://www.linkedin.com/search/results/content/?keywords=justmyroots&origin=GLOBAL_SEARCH_HEADER&sid=jtm")

sign_in=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,'Sign in'))).click()

user_name=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'username')))
user_name.clear()
user_name.send_keys('smartiswarchand@gmail.com')

password=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'password')))
password.clear()
password.send_keys('kgs18101998',Keys.ENTER)

# You can set your own pause time. My laptop is a bit slow so I use 1 sec

screen_height = driver.execute_script(
    "return window.screen.height;")  # get the screen height of the web
i = 1

for count in range(20):
    # scroll one screen height each time
    driver.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(num)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script(
        "return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break


divs = driver.find_elements_by_xpath(
    '//div[@class="occludable-update ember-view"]')
for div in divs:
    try:
        send = div.find_element_by_css_selector("div.send-privately-button > button")
        driver.execute_script("arguments[0].click();", send)
        link = driver.find_element_by_xpath('/html/body/div[6]/aside/div[2]/div[1]/form/div/div/div[3]/div[2]/a').get_attribute('href')
        link_linkedin.append(link)
        driver.find_element_by_xpath('//button[@data-control-name="overlay.close_conversation_window"]').click()
    except Exception:
        continue
print(link_linkedin)
df = pd.DataFrame({'Links': link_linkedin})
df.to_csv('linkedIn_jmr_AUG_TO_NOV.csv', index=False)  

# print(link_linkedin)



