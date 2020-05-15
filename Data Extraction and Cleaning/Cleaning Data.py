'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 2

References:
https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf
'''
import sys
import csv
import re
import string
import pymongo

values = []

fall= open('Tweets_Cleaned.csv', 'w', encoding="utf-8",newline='')
wrall = csv.writer(fall)

fall2= open('News_Cleaned.csv', 'w', encoding="utf-8",newline='')
wrall2 = csv.writer(fall2)

pr = set(string.printable)

#Regular Expression to detect emoticons
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

mdbclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = mdbclient["db2"]
col = db["assignment2_tweets"]

with open("Tweets.csv",encoding='utf8',newline='') as obj:
    read = csv.reader(obj)
    st=0
    for row in read:
        cnt=0
        ls=[]
        dict={}
        for val in row:
            
            #Step 1 from Report [Cleaning Process - new lines (‘\n’)]
            val=val.replace("\n",";")
            #Step 2 from Report [Cleaning Process - hyperlink(s)]
            test=re.sub(r"http\S+", "", val)
            #Step 3 from Report [Cleaning Process - emoticons]
            test=emoji_pattern.sub(r'', test)
            #Step 4 from Report [Cleaning Process - non-ascii codes]
            test = re.sub(r'[^\x00-\x7F]+',' ', test)
            #Step 5 from Report [Cleaning Process - BLANK values]
            if(len(test)==0):
                test='NaN'
            #Step 6 from Report [Cleaning Process - Special and non-printable characters]
            test=''.join(filter(lambda x: x in pr, test)).replace('\\d','')

            ls.append(test)

            if(cnt==0):
                dict['UserName']=test
            elif(cnt==1):
                dict['Time']=test
            elif(cnt==2):
                dict['Tweet']=test
            elif(cnt==3):
                dict['Location']=test
            elif(cnt==4):
                dict['Retweets']=test
            elif(cnt==5):
                dict['Favorites']=test

            cnt+=1

        #Step 7 from Report [Cleaning Process - CSV File]
        wrall.writerow(ls)

        #print(dict)

        #Step 8 from Report [Cleaning Process - MongoDB]
        if(st==1):
            col.insert_one(dict)

        st=1

col = db["assignment2_news"]
    
with open("News.csv",encoding='utf8',newline='') as obj:
    read = csv.reader(obj)
    st=0
    for row in read:
        cnt=0
        ls=[]
        dict={}
        for val in row:

            #Step 1 from Report [Cleaning Process - new lines (‘\n’)]
            val=val.replace("\n",";")
            #Step 3 from Report [Cleaning Process - emoticons]
            test=emoji_pattern.sub(r'', val)
            #Step 4 from Report [Cleaning Process - non-ascii codes]
            test = re.sub(r'[^\x00-\x7F]+',' ', test)
            #Step 5 from Report [Cleaning Process - BLANK values]
            if(len(test)==0):
                test='NaN'
            test=''.join(filter(lambda x: x in pr, test)).replace('\\d','')
            ls.append(test)

            if(cnt==0):
                dict['Source']=test
            elif(cnt==1):
                dict['Author']=test
            elif(cnt==2):
                dict['Title']=test
            elif(cnt==3):
                dict['Description']=test
            elif(cnt==4):
                dict['URL']=test
            elif(cnt==5):
                dict['Published At']=test
            elif(cnt==6):
                dict['Content']=test
            cnt+=1

        #Step 6 from Report [Cleaning Process - CSV File]
        wrall2.writerow(ls)
        
        #print(dict)

        #Step 7 from Report [Cleaning Process - MongoDB]
        if(st==1):
            col.insert_one(dict)

        st=1
