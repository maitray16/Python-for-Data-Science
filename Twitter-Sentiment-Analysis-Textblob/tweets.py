import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'Consumer Key (API Key)'
consumer_secret= 'Consumer Secret (API Secret)'

access_token='Access Token'
access_token_secret='Access Token Secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('MLK')

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
