'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 3

References:
[1] Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." 
       Proceedings of the ACM SIGKDD International Conference on Knowledge 
       Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, 
       Washington, USA,
    Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
       and Comparing Opinions on the Web." Proceedings of the 14th 
       International World Wide Web conference (WWW-2005), May 10-14, 
       2005, Chiba, Japan.

    Available:  https://gist.github.com/mkulakowski2/4289437#file-positive-words-txt
                https://gist.github.com/mkulakowski2/4289441#file-negative-words-txt

'''
import sys
import csv
import re
import string
import pymongo
import pandas as pn

no = []
msg = []
match = []
polarity = []
positives = []
negatives = []

lst = []

pos=[]
neg=[]

cnt=0

#[1]
with open('.\\Words\\positive-words.txt', 'r') as f:
    pos = [line.strip().lower() for line in f]
#[1]
with open('.\\Words\\negative-words.txt', 'r') as f:
    neg = [line.strip().lower() for line in f]

with open(".\\Tweet_Data\\Tweets_Cleaned.csv",encoding='utf8',newline='') as obj:
    read = csv.reader(obj)
    
    for row in read:
        cnt += 1        
        
        col_filter=0
        dict={}
        for tweet in row:
            if(col_filter == 2):

                no.append(cnt)
                msg.append(tweet)
                
                split_tweet = tweet.split(' ')
                for val in split_tweet:
                    val = val.lower()
                    
                    #Step - 3: Bag of Words for each tweet
                    if(val in dict.keys()):
                        dict[val] += 1
                    else:
                        dict[val] = 1
                  
            col_filter += 1    
        lst.append(dict)

worddict = {}
word = []
wcnt = []
wnature = []

for dict in lst:
    posword = 0
    negword = 0
    words=''

    for key in dict.keys():
        key = key.lower()
        if(key in pos):
            posword+=dict[key]
            words+=key+', '

            #Bag of Words for all tweets
            if(key in worddict.keys()):
                worddict[key] += dict[key]
            else:
                worddict[key] = dict[key]
                
        elif(key in neg):
            negword+=dict[key]
            words+=key+', '

            #Bag of Words for all tweets
            if(key in worddict.keys()):
                worddict[key] += dict[key]
            else:
                worddict[key] = dict[key]

    #Step - 4, 5: Polarity check for each tweet and tagging
    if(posword>negword):
        polarity.append('positive')
    elif(posword<negword):
        polarity.append('negative')
    elif(posword==negword):
        polarity.append('neutral')

    if(len(words)==0):
        words='NA, '

    match.append(words[0:len(words)-2])
    positives.append(posword)
    negatives.append(negword)

for key in worddict.keys():
    word.append(key)
    wcnt.append(worddict[key])
    #Nature check for the words in the bag (for all the tweets)
    if(key in pos):
        wnature.append('postitive')
    elif(key in neg):
        wnature.append('negative')


df = pn.DataFrame({'Tweet':no, 'message':msg, 'match':match, 'polarity':polarity, 'positives':positives, 'negatives':negatives})
df.to_csv('Tweets_Polarity.csv', index=False, encoding='utf-8')
df.to_excel('Tweets_Polarity.xlsx', engine='xlsxwriter')


df = pn.DataFrame({'Word':word, 'Frequency':wcnt, 'Nature':wnature})
df.to_csv('Word_Cloud_Data.csv', index=False, encoding='utf-8')
df.to_excel('Word_Cloud_Data.xlsx', engine='xlsxwriter')
