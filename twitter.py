
import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
import time

tweets_list2 = []



# count = 0


# for keyword in keywords[6:]:
        
#     print(keyword)
#     # Using TwitterSearchScraper to scrape data and append tweets to list
#     for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} near:"indore" since:2021-11-1 until:2021-12-16').get_items()):
#     # =============================================================================
#     #     if i>500:
#     #         break
#     # =============================================================================
#         # tweets_list2 = []
#         name = tweet.user.username
#         if name != 'Just_My_Roots':
#             tweets_list2.append([tweet.date,tweet.url, tweet.user.username])
#     count = count+1
#     time.sleep(5)        

# Flurys - Rum Plum Cake
# Flurys - Dundee Cake 
# Venus - Nut Rich Plum Cake
# A1 Bakery - Choco Walnut Cake
# A1 Bakery - Mawa Cake 
# A1 Bakery - Plum Cake
# Saldanha Bakery - Fruit Cake 
#christmas cake


#keywords = ['Mouthwatering','Delectable','yummy','Delicious','Delightful','Divine','Dulcet','Dulcified','Edible', 'Enjoyable','Enticing',
#'Fantastic','Finger-licking','Flavored','Flavorful','Flavorsome','Juicy','Luscious','Lush', 'Marvelous',
#'Nectarous','Refreshing','Satisfying','Saute','Savory','Spicy','Sour','Smooth','Lip-smacking', 'crusty', 'fried','Toothsome','tasty']

tweets_list2 = []

keyword = 'Nut Rich Plum Cake'
    
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} near:jaipur since:2021-11-18 until:2021-12-18').get_items()):
# =============================================================================
#     if i>500:
#         break
# =============================================================================
    # tweets_list2 = []
    name = tweet.user.username
    if name != 'Just_My_Roots':
        tweets_list2.append([tweet.date,tweet.url, tweet.user.username])

print(len(tweets_list2))

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime','Link', 'Username'])
tweets_df2.to_csv('jaipur_cake.csv',sep=',', encoding='utf8', index=False)


# print(count)





