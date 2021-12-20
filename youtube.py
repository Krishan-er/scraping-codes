# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:51:27 2021

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
import os
import random 
import requests as rq
from random import randint
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


link_set = set()
option = Options()
option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

#option.add_argument("--headless")
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.youtube.com/results?search_query=shahi+paneer+recipe')

# You can set your own pause time. My laptop is a bit slow so I use 1 sec
scroll_pause_time = 1
screen_height = driver.execute_script(
    "return window.screen.height;")  # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script(
        "return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break


links = driver.find_elements_by_xpath('//div[@id="channel-info"]//a[@dir="auto"]')
for item in links:
    link = item.get_attribute("href")
    link_set.add(link)


links_list = list(link_set)
    
df = pd.DataFrame({'Links': links_list})
df.to_csv('youtube_links.csv', index=False)


 























