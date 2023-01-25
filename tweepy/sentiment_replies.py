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

# Define the username of the user whose tweets you want to get replies for
username = "adam22"

# Get the user's tweets
tweets = api.user_timeline(screen_name=username)

# Set up AWS Comprehend client
session = boto3.Session(
    aws_access_key_id = config.aws_access_key,
    aws_secret_access_key = config.aws_access_key_secret,
    region_name='us-east-1'
)
comprehend = session.client('comprehend')
dynamodb = session.client('dynamodb')

# Analyze sentiment of tweet text data
for tweet in tweets:
    print("------------------------------")
    print("Replies for tweet: ",tweet.text)
    print("------------------------------")
    for reply in tweepy.Cursor(api.search_tweets,q='to:'+username, since_id=tweet.id).items(1000):
        if hasattr(reply, 'in_reply_to_status_id_str'):
            if (reply.in_reply_to_status_id_str==tweet.id_str):
                print(reply.text)
                sentiment = comprehend.detect_sentiment(Text=reply.text, LanguageCode='en')
                print("Sentiment: ", sentiment["Sentiment"])
                print("------------------------------")




