'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 2

https://newsapi.org/docs/client-libraries/python

'''

from newsapi import NewsApiClient
import pandas as pn

#Step 13 from Report [Data Extraction Process - API key]
newsapi = NewsApiClient(api_key='af3e7fd5a8a24bba9798f43308b09558')

source=[]
author=[]
title=[]
description=[]
url=[]
publishedAt=[]
content=[]
items=[]

#Step 14 from Report [Data Extraction Process - word filter]
words = "Canada OR University OR Dalhousie University OR Halifax OR Canada Education"

page_cnt=5

#Step 15 from Report [Data Extraction Process - page loop]
for i in range(1,page_cnt+1):
    
    articles = newsapi.get_everything(q=words,language='en',sort_by='relevancy',page=i)

    #Step 16 from Report [Data Extraction Process - Retrieved JSON data]
    for ar in articles["articles"]:

        #Step 17 from Report [Data Extraction Process - Append data]
        source.append(ar['source']['name'])

        author.append(ar['author'])

        title.append(ar['title'])

        description.append(ar['description'])

        url.append(ar['url'])

        publishedAt.append(ar['publishedAt'])

        content.append(ar['content'])

#Step 18 from Report [Data Extraction Process - CSV file]
df = pn.DataFrame({'Source':source,'Author':author,'Title':title,'Description':description,'URL':url,'Published At':publishedAt,'Content':content})
df.to_csv('News.csv', index=False, encoding='utf-8')

