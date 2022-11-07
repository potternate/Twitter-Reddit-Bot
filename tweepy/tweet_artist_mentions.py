import tweepy
import config
from sentiment import sent
import pandas as pd

client = tweepy.Client(config.bearer_token, config.api_key, config.api_secret, config.access_token, config.access_token_secret)

artist = 'A Boogie'
project = 'single "Ballin"'
query = artist + ' (-is:retweet -is:reply)'

start_time = '2022-11-03T04:00:00Z'
end_time = '2022-11-04T04:00:00Z'

counts = client.get_recent_tweets_count(query=query, granularity='day', start_time=start_time, end_time=end_time)

total = 0
for count in counts.data:
    total += count['tweet_count']

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
api.update_status(artist + ' mentioned in ' + str(total) + ' tweets in 24 hours following release of ' + project)
