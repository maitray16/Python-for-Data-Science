import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'ih5NsEp8ySy2OKHnkrCICH6i9'
consumer_secret= 'oDiyriuVwSJEJkxuVBQkBjFP7S094fsJfhy9435wgeecvwMhxY'

access_token='903635598-FbBtOCFbzzth4EHyVtS4SO6y0T07J8LPmmoWb191'
access_token_secret='PUTwzw9keEN3jEdkLsVPqwXklaIxdxk6lIyaVaAHQtvCa'

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
