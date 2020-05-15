'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 3

References:
[1] D. Jayasekara, “Extracting Twitter Data, Pre-Processing and Sentiment Analysis using Python”
    Medium, 03-Apr-2019. [Online].
    Available: https://towardsdatascience.com/extracting-twitter-data-pre-processing-and-sentiment-analysis-using-python-3-0-7192bd8b47cf. [Accessed: 04-Dec-2019].

Note:
Cleaning had already been done in the Assignment 2. This file has been created with the reference of the cleaning script submitted under assignment 2.
'''
import sys
import csv
import re
import string

values = []

fall= open('.\\Tweet_Data\\Tweets_Cleaned.csv', 'w', encoding="utf-8",newline='')
wrall = csv.writer(fall)

pr = set(string.printable)

with open(".\\Tweet_Data\\Tweets.csv",encoding='utf8',newline='') as obj:
    read = csv.reader(obj)
    st=0
    for row in read:
        cnt=0
        ls=[]
        dict={}
        for val in row:
            #clean new lines (‘\n’)
            val = val.replace("\n",";")
            #clean "RT" 
            val = val.replace("RT","")
            #clean usernames
            test = re.sub(r'[@]\w+','', val)
            #clean hyperlink(s) [1]
            test = re.sub(r"http\S+", "", test.replace(' : ',''))
            #clean non-ascii codes [1]
            test = re.sub(r'[^\x00-\x7F]+',' ', test)
            #clean BLANK values [1]
            if(len(test)==0):
                test='NaN'
            #clean special and non-printable characters [1]
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

        wrall.writerow(ls)

        st=1
