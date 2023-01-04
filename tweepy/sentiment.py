import tweepy
import boto3
import config

# Set up your Twitter API credentials
consumer_key = config.api_key
consumer_secret = config.api_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Retrieve tweet text data
tweets = api.user_timeline(screen_name='adam22', count=100)
tweet_texts = [tweet.text for tweet in tweets]

# Set up AWS Comprehend client
session = boto3.Session(
    aws_access_key_id = config.aws_access_key,
    aws_secret_access_key = config.aws_access_key_secret,
    region_name='us-east-1'
)
comprehend = session.client('comprehend')

# Analyze sentiment of tweet text data
for text in tweet_texts:
    sentiment = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    print(f'Tweet text: {text}\nSentiment: {sentiment["Sentiment"]}\n')