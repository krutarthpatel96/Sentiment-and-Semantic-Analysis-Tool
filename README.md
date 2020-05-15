# Sentiment-and-Semantic-Analysis-Tool

**Data Extraction Process [3400 Tweets + 100 News Articles (due to free API usage limit)]**

Searching API [1]

1. Created developer account on Twitter

2. Generated and used authentication tokens (consumer key, consumer secret, access token key, access token secret)

3. Performed authentication using consumer key and consumer secret

4. Provided my access token and access token secret.

5. Created a word filter

6. Used tweepy cursor to make use of Twitter Searching API and get JSON data (extracted 1700 tweets)

7. Append data into a list


Streaming API [2]

8. Implemented a stream listener with word filters that provides real time data. (extracted 1700 tweets)

9. Used onStatus method to get twitter data (onData can also be used to get the tweets in string format)

10. Append data into the list

11. Saved it as a CSV file

NewsAPI [3]

12. Created a developer account on NewsAPI

13. Generated and used API key

14. Created a word filter

15. Implemented a page loop since the data is provided in pages (~20 news per page)

16. Retrieved JSON data

17. Append data into the list

18. Saved it as a CSV file



**Data Cleaning**

1. Replaced new lines (‘\n’) with (‘’) to make sure that the data is imported in a proper manner in Spark dataframe

2. Removed hyperlink(s) from the tweets

3. Removed emoticons

4. Removed non-ascii codes such as ‘\xa3’, ‘\xc2’ etc.

5. Replaced BLANK values with NaN

6. Removed special and non-printable characters

7. Saved cleaned data in a CSV file

8. Stored cleaned data in MongoDB



**Bag of words**
1. Read the tweets from the csv file.

2. Split the words by ‘ ’(space).

3. Create a data dictionary that takes the words as keys and their occurrences as value.

4. Iterate through all the tweets and save the occurrences of the words.



**Polarity Tagging**
1. Download a word list of positive and negative words from the internet.

2. Read the files and save the words in two separate lists – positive and negative

3. After the occurrences of the words have been determined using the bag of words, check the presence of each word from the bag in the positive and negative word list.

4. If the word exists in the positive list, set its polarity to ‘positive’ and vice-versa.



**Tableau**

1. Upload the csv file that contains the words, its occurrences in the tweets, and its nature (positive or negative) in Tableau.

2. Use word as label, occurrence as size, and nature as colour.

3. Use red colour for negative words and green colour for positive words.

Result: Most frequently used word: positive: free, negative: poor



**Semantic Analysis**

Transformation

1. Read the articles from the csv file.

2. Extract three columns – Title, Description, and Content.

3. Create individual text files using pandas for each article.



**Calculating required measures**

1. Use lists to store the frequency, presence count of each word in the documents.

2. Use a variable to store the total number of documents used.

3. Use Math library to use log function.

4. Save the data in csv files as required.



References:
[1] “Cursor Tutorial,” Cursor Tutorial - tweepy 3.5.0 documentation. [Online]. Available: http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html. 
[2] “Getting started,” Getting started - tweepy 3.5.0 documentation. [Online]. Available: http://docs.tweepy.org/en/v3.5.0/getting_started.html. 
[3] “News API - A JSON API for live news and blog articles,” News API - A JSON API for live news and blog articles. [Online]. Available: https://newsapi.org/.
