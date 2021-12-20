# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:20:03 2021

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
from random import randint
import html5lib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import csv


with open("Insta_post.csv", mode="w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Name','Link','Post'])

option = Options()
option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(options=option, executable_path='./chromedriver.exe')
driver.get('https://www.instagram.com')
time.sleep(3)
mail_id = driver.find_element_by_xpath('//input[@name="username"]')
mail_id.send_keys('xyzishwar@gmail.com')
mail_id.send_keys(Keys.TAB)

password = driver.find_element_by_xpath('//input[@name="password"]')
password.send_keys('kgs18101998')
password.send_keys(Keys.ENTER)
time.sleep(10)

notnow = driver.find_element_by_xpath('//button[contains(text(),"Not Now")]')
notnow.click()

df = pd.read_csv('Insta_justmyroots_AUG_TO_NOV.csv')

for link in df['Links']:
    try:
        driver.get(link)
        time.sleep(1)
        data = []
        name = driver.find_element_by_xpath('(//span[@class="Jv7Aj mArmR MqpiF  "])[1]').text
        if name != 'just_my_roots':
            post = driver.find_element_by_xpath('(//div[@class="C4VMK"])[1]')
            post = post.text
            data.append(name)
            data.append(link)
            data.append(post)
            with open("Insta_post.csv", mode="a", newline="", encoding='utf-8') as output_file:
                writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(data)
    
    except Exception:
        pass
    
                


