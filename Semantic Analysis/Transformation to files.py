'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 3

'''
import csv
import pandas as pn

cnt=0

with open(".\\News_Data\\News_Cleaned.csv",encoding='utf8',newline='') as obj:
    read = csv.reader(obj)

    for row in read:
        title = []
        desc = []
        content = []

        cnt += 1        
        col_filter=0

        #Step 9 - Column Extraction
        for news in row:
            if(col_filter == 2):
                title.append(news)
    
            elif(col_filter == 3):
                desc.append(news)

            elif(col_filter == 6):
                content.append(news)

            col_filter+=1

        if(cnt>1):
            #Step 8 - Create individual file for each article
            strname = str((cnt-1))+".txt"
            df = pn.DataFrame({'Title':title, 'Description':desc, 'Content':content})
            df.to_csv(".\\News_Data\\Files\\"+strname, index=False, encoding='utf-8', header=False)
        
