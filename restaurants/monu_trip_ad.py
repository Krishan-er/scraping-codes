# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:48:32 2021

@author: kgs1
"""

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import lxml
import pandas as pd

from requests_html import HTMLSession
session = HTMLSession()


import time

import unidecode
import csv


# page_list = []
# # pagination (will fetch the link of the pagination )
# for page in range(0,630,30):
#     page_url = f'https://www.tripadvisor.in/Restaurants-g304551-oa{page}-New_Delhi_National_Capital_Territory_of_Delhi.html'
#     page_list.append(page_url)
    
 

# Loading trip adviser restaurant data

driver = webdriver.Chrome(executable_path='scripts/chromedriver.exe')


# saving data into csv
with open("chennai_ta.csv", mode="w", newline="", encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(
        ['title', 'location', 'Review', 'Rating' 
         ])


# csv writter
def write_output(data):
    with open('chennai_ta.csv', mode='a',encoding='utf-8',newline='') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)
            

# Handle the exception and write the exception
def fail_data(link,error):
    df1  = pd.DataFrame({
        'url' : [link],
        'error' : [error],
    })
    df1.to_csv('fail_data.csv', mode = 'a', index = False, header=False, encoding  = 'utf-8-sig')

    


def fetch_data(link):
    u = link
    print(u)
    try:
        # r1 = session.get(u)
        # print(r1)
        driver.get(u)
        soup = bs(driver.page_source, 'html5lib')
        #soup = bs(r1.text, 'html5lib')
        
        # title
        try:
            title = soup.find('h1', class_="fHibz").text.strip()
        except:
            title = ''
        #print(title)
        
        # location
        try:
            #loc = soup.find('a', class_="fhGHT")[2].text.strip()
            loc = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'(//a[@class="fhGHT"])[2]')))
            loc = loc.text
        except:
            loc = ''
        #print(loc)
       
        
        # review
        try:
            review = soup.find('span', class_="eBTWs").text.replace('reviews', '').replace('review', '').strip()
        except:
            review = ''
        #print(review)
       
        # rating
        try:
            rating = soup.find('svg', class_="RWYkj d H0")['title'].split(' ')[0].strip()
        except:
            rating = ''
        #print(rating)
      

        restaurant = []
        restaurant.append(title)
        restaurant.append(loc)
        restaurant.append(review)
        restaurant.append(rating)
        restaurant = [str(x).replace("\n", ' ').replace("\t", '').replace("\r", '').strip() if x else '' for x in restaurant]
        print(restaurant)
        write_output([restaurant])
        
    except Exception as e:
        fail_data(str(u), str(e))
    time.sleep(0.6)
        
        

def scrape():  
    df = pd.read_csv('chennai_url_ta.csv')
    for rest in list(df['Restaurnat_url'])[:200]:
        fetch_data(rest)
scrape()



    
    
    

    
    
    


    
