import tweepy
import config
from sentiment import sent
import pandas as pd

client = tweepy.Client(config.bearer_token, config.api_key, config.api_secret, config.access_token, config.access_token_secret)

artist = 'Lil Uzi Vert'
project = 'music video "Just Wanna Rock"'
query = artist + ' (-is:retweet -is:reply)'
cover_art = "justwannarock_mv.jpeg"

start_time = '2022-11-18T04:00:00Z'
end_time = '2022-11-19T04:00:00Z'

counts = client.get_recent_tweets_count(query=query, granularity='day', start_time=start_time, end_time=end_time)

total = 0
for count in counts.data:
    total += count['tweet_count']

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)
api.update_status_with_media(status = artist + ' mentioned in ' + str(total) + ' tweets in 24 hours following release of ' + project, filename = cover_art)

