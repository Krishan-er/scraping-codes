# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:35:42 2021

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
import csv

# with open("Youtuber_data1.csv", mode="w", newline="", encoding='utf-8') as output_file:
#     writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
#     writer.writerow(['Name','Subscribers','Link'])
# output_file.close()

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


df = pd.read_csv('youtube_links.csv')
for link in df['Links']:
    data = []
    driver.get(link)
    time.sleep(2)
    name = driver.find_element_by_xpath('(//div[@id="text-container"]/yt-formatted-string)[1]')
    name = name.text
    subscribers = driver.find_element_by_xpath('//*[@id="subscriber-count"]').text
    data.append(name)
    data.append(subscribers)
    data.append(link)

    with open("Youtuber_data1.csv", mode="a", newline="", encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=",",
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(data)
        
    output_file.close()
    

















