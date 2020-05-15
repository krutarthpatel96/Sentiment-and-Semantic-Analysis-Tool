'''
Name: Patel Krutarth
Banner ID: B00835794
Course: CSCI-5708
Purpose: Assignment 2

References:
http://docs.tweepy.org/en/latest/getting_started.html#api
http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html
https://www.w3schools.com/python/python_mongodb_insert.asp
'''
import tweepy
import csv
import pandas as pn
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Step 2 from Report [Data Extraction Process - authentication tokens]
consumer_key = 'yzqfwuW4jw6Z37xzRx8nl9biR'
consumer_secret = 'qI95GKBczRvPgmbLLKzrNGZRnZkgF4x1CxJUI1MztC8i8U0tlX'
access_token = '507134513-w94AhxgdHPBIcQtbexIiToCFxl8pilgQjaCL2M3M'
access_token_secret = '4Lh4CfNPYzWrOkS4pvgTQNtLBz9ON7peEiNN5EAQdhwWt'

#Step 3 from Report [Data Extraction Process - Performed Authentication]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

#Step 4 from Report [Data Extraction Process - Provided my acess token]
auth.set_access_token(access_token, access_token_secret)

tw_api = tweepy.API(auth,wait_on_rate_limit=True)

username=[]
time=[]
tweets=[]
loc=[]
retweet_cnt=[]
favor_cnt=[]
replied=[]
max=10

#Step 5 from Report [Data Extraction Process - word filter]
words = "Canada OR University OR 'Dalhousie University' OR Halifax OR'Canada Education'"

#Step 6 from Report [Data Extraction Process - Searching API]
for tweet in tweepy.Cursor(tw_api.search,q=words,lang="en").items(1700):

    #Step 7 from Report [Data Extraction Process - Append data]
    
    #Username/ScreenName
    username.append(tweet.user.screen_name)
    #Time
    time.append(tweet.created_at)
    #Tweet
    tweets.append(tweet.text)
    #Location
    loc.append(tweet.user.location)
    #Retweet Count
    retweet_cnt.append(tweet.retweet_count)
    #Favorite Count
    favor_cnt.append(tweet.favorite_count)
    #Reply Count
    replied.append(tweet.in_reply_to_status_id_str)

#Step 8 from Report [Data Extraction Process - Streaming API]
class listener(StreamListener):
    cnt=0

    #Step 9 from Report [Data Extraction Process - onStatus method]
    def on_status(self, status):

        #Step 10 from Report [Data Extraction Process - Append Data]

        if(self.cnt<1700):
            #Username/ScreenName
            username.append(status.user.screen_name)
            #Time
            time.append(status.created_at)
            #Tweet
            tweets.append(status.text)
            #Location
            loc.append(status.user.location)
            #Retweet Count
            retweet_cnt.append(status.retweet_count)
            #Favorite Count
            favor_cnt.append(status.favorite_count)
            #Reply Count
            replied.append(status.in_reply_to_status_id_str)

            self.cnt+=1
            
        else:
            return False

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Canada","University","Dalhousie University","Halifax","Canada Education"])

'''
print(username)
print(time)
print(tweets)
print(loc)
print(retweet_cnt)
print(favor_cnt)
print(replied)
'''

#Step 11 from Report [Data Extraction Process - CSV file]
df = pn.DataFrame({'User Name':username,'Time':time,'Tweet':tweets,'User Location':loc,'Retweeted Count':retweet_cnt,'Favorited Count':favor_cnt,'Replied':replied})
df.to_csv('Tweets.csv', index=False, encoding='utf-8')
