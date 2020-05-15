'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 3

References:
[1]     Author: adamk
        Available: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
'''
import sys
import csv
import re
import string
import pymongo
import pandas as pn
import math
import os,glob

query = []
query.append('Canada')
query.append('University')
query.append('Dalhousie University')
query.append('Halifax')
query.append('Canada Education')

df = [0, 0, 0, 0, 0]
ndf = [0, 0, 0, 0, 0]
totdocs = 0
logdf = [0, 0, 0, 0, 0]

cnt=0

arno = []
ar = []
freqcanada = []
totwords = []
rf = []

arno_maxrf = 0
article_maxrf = ''
maxrfval = 0

all_files=[]

#[1]
for newsfile in glob.glob(os.path.join(".\\News_Data\\Files\\", '*.txt')):
    all_files.append(int(newsfile[newsfile.rindex('\\')+1:newsfile.rindex('.')]))

all_files.sort()

#Read all files
for newsfile in all_files:
    cnt += 1

    target_file = '.\\News_Data\\Files\\'+str(newsfile)+'.txt'

    #Open each file
    with open(target_file,encoding='utf8',newline='') as obj:
        read = csv.reader(obj)

        for row in read:
            col_filter=0
            for news in row:
                if(col_filter == 2):

                    article = news

                    #Step 10(a): Word presence count 
                    if('canada' in news.lower()):
                        df[0]+=1
                    if('university' in news.lower()):
                        df[1]+=1
                    if('dalhousie university' in news.lower()):
                        df[2]+=1
                    if('halifax' in news.lower()):
                        df[3]+=1
                    if('canada education' in news.lower()):
                        df[4]+=1

                    #Step - 10(b): Frequency count of canada in the article
                    can = news.lower().count('canada')

                    if(can>0):
                        #Step - 10(b)Total words in the article
                        wordcnt = len(news.split())
                        
                        arno.append(cnt)
                        freqcanada.append(can)
                        totwords.append(wordcnt)
                        #Relative Frequency
                        rfval = can/wordcnt

                        #Step - 10(c): Max relatice frequency check
                        if(rfval > maxrfval):
                            arno_maxrf = cnt
                            maxrfval = rfval
                            article_maxrf = article

                        ar.append(article)
                        rf.append(rfval)
                        
                col_filter += 1

query.append('')
df.append('')
ndf.append('')
logdf.append('')
query.append('Total documents(N): ')
query[6] += str(cnt)
df.append('')
ndf.append('')
logdf.append('')

arno.append('')
ar.append('')
totwords.append('')
freqcanada.append('')
rf.append('')
arno.append('Max Relative Frequency: '+str(maxrfval))
ar.append('')
totwords.append('')
freqcanada.append('')
rf.append('')
arno.append('Article No: '+str(arno_maxrf))
ar.append('')
totwords.append('')
freqcanada.append('')
rf.append('')
arno.append('Article: '+str(article_maxrf))
ar.append('')
totwords.append('')
freqcanada.append('')
rf.append('')

#Step - 10(c): Print the max. relative frequency with relevant details
print('Max Relative Frequency: '+str(maxrfval))
print('\nArticle no: '+str(arno_maxrf))
print('\nArticle: '+str(article_maxrf))

#Step 10(a): Calculation of df and Log10(N/df)
for i in range(0,len(query)-2):
    if(df[i]>0):
        ndf[i] = cnt/df[i]
        logdf[i] = math.log10(cnt/df[i])
    else:
        ndf[i] = 'Undefined'
        logdf[i] = 'Undefined'

df = pn.DataFrame({'Search Query':query, 'Documents containing term (df)':df, 'Total Documents(N)/ number of documents term appeared(df)':ndf, 'Log10(N/df)':logdf})
df.to_csv('News_TF-IDF.csv', index=False, encoding='utf-8')

df = pn.DataFrame({'#Article':arno, 'Article':ar, 'Total Words (m)':totwords, 'Frequency (f)':freqcanada,'Relative Frequency (f/m)':rf})
df.to_csv('News_Frequency.csv', index=False, encoding='utf-8')
