# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:03:41 2021

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


# Flurys - Rum Plum Cake
# Flurys - Dundee Cake 
# Venus - Nut Rich Plum Cake
# A1 Bakery - Choco Walnut Cake
# A1 Bakery - Mawa Cake 
# A1 Bakery - Plum Cake
# Saldanha Bakery - Fruit Cake 
#christmas cake


# nolen gur
# jhola gur
# patali gur
# khejur gur
# date palm jaggery
# khajoor gur
# jaggery



option = Options()
links_list = []
option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

#option.add_argument("--headless")
driver=webdriver.Chrome(executable_path='./chromedriver.exe',options=option)
driver.get('https://www.facebook.com')
mail_id = driver.find_element_by_id('email')
mail_id.send_keys('mail')
mail_id.send_keys(Keys.TAB)

password = driver.find_element_by_id('pass')
password.send_keys('pass')
password.send_keys(Keys.ENTER)

LOCATION = 'indore'
keyword = ''

search = driver.find_element_by_xpath("//input[@type='search']")
search.send_keys(keyword)
time.sleep(2)
action = ActionChains(driver)
opt = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,f'Search for {keyword}')))
opt.click()
#opt = driver.find_element_by_xpath("//a[@role='presentation']")
#action.move_to_element(opt).click().perform()
time.sleep(2)
post = driver.find_element_by_link_text('Posts').click()
see_all = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,f"//span[contains(text(),'See all public posts for \"{keyword}\"')]")))
see_all.click() 
recent_posts = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@aria-label="Recent posts"]')))
recent_posts.click()
scroll_pause_time = 2  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web

tagged_location = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Tagged location')]")))
tagged_location.click()
enter_location = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//input[@placeholder="Choose a location..."]')))
enter_location.send_keys(LOCATION)
time.sleep(2)
enter_location.send_keys(Keys.DOWN)
enter_location.send_keys(Keys.ENTER)

# last_height = driver.execute_script("return document.body.scrollHeight")

# for i in range(30):
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(scroll_pause_time)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

links_list = []

data = bs(driver.page_source,'lxml')
links = data.find_all('a',class_='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb n00je7tq arfg74bv qs9ysxi8 k77z8yql btwxx1t3 abiwlrkh p8dawk7l lzcic4wl a8c37x1j tm8avpzi')
for item in links:
    link = item['href']
    # print(link)
    links_list.append(link)
    
df = pd.DataFrame({'links':links_list})
df.to_csv('indore_fb_data.csv',mode = 'a',index=False)
    
driver.close()
