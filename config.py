import tweepy
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger()


def create_api():
    api_key = os.environ.TWITTER_API_KEY
    api_key_secret = os.environ.TWITTER_API_KEY_SECRET
    access_token = os.environ.TWITTER_ACCESS_TOKEN
    access_token_secret = os.environ.TWITTER_ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
