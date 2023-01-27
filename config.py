import tweepy
import logging

logger = logging.getLogger()


def create_api():
    consumer_key = 'kjPmXkwmi6MVrYdOi6PtNSTxr'
    consumer_secret = 'vRZKJ3QTLh58TWRdEIm8O4RAKOAxxh9OliwbxAdBmjW31iwsr3'
    access_token = '773736831112339456-KMSYlbxp8k5oSONBc9i3XDzjzP8SRJM'
    access_token_secret = 'jMlasQSOcvHYMV90sw7tbLo5fACrEYVeQUXHPWWa7tI95'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
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
