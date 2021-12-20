# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:05:34 2021

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


first = 'https://www.instagram.com'
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

link_set = set()

search = driver.find_element_by_xpath('//input[@placeholder="Search"]')
search.send_keys('#nolengur')
time.sleep(2)
action = ActionChains(driver)
opt = driver.find_element_by_xpath("//a[@class='-qQT3']")
action.move_to_element(opt).click().perform()
time.sleep(8)
scroll_pause_time = 3  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web

y = 1000
for i in range(20):
    driver.execute_script("window.scrollTo(0, " + str(y) + ")")
    y += 1000
    num = randint(3, 6)
    time.sleep(num)
    soup = bs(driver.page_source, 'html5lib')
    link_container = soup.find_all('a', {"tabindex": "0"})
    #print(len(link_container))
    for item in link_container:
        link = item['href']
        sequence = (first, link)
        hl = ''.join(sequence)
        link_set.add(hl)
    soup.decompose()
        
print(link_set)
link_list = list(link_set)

df = pd.DataFrame({'Links': link_list})
df.to_csv('nolen_gur.csv', index=False)  
 


