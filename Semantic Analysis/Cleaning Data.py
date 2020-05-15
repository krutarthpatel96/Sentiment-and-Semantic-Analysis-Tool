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

fall2= open('.\\News_Data\\News_Cleaned.csv', 'w', encoding="utf-8",newline='')
wrall2 = csv.writer(fall2)

pr = set(string.printable)
    
with open(".\\News_Data\\News.csv",encoding='utf8',newline='') as obj:
    read = csv.reader(obj)
    st=0
    for row in read:
        cnt=0
        ls=[]
        dict={}
        for val in row:

            #clean new lines (‘\n’)
            val=val.replace("\n",";")
            #clean non-ascii codes [1]
            test = re.sub(r'[^\x00-\x7F]+',' ', val)
            #clean BLANK values [1]
            if(len(test)==0):
                test='NaN'
            #clean special and non-printable characters [1]
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
                test=re.sub(r"http\S+", "", val)
                dict['Content']=test
            cnt+=1

        wrall2.writerow(ls)

        st=1
