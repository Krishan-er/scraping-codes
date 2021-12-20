# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:35:16 2021

@author: kgs1
"""

import googlesearch
from newspaper import Article
import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()

query = "Polyimide Foam manufacturers in india"

search = googlesearch.search(query , lang='en',country = 'India', pause=1, stop=30)
df = pd.DataFrame({'sites': search})
df.to_csv('foam_url.csv', index=False)

