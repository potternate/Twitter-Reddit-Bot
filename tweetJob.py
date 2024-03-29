import random
import requests
from config import create_api, create_reddit_instance
import os
import regex
from customFeed import subreddits

# Create Twitter API
api = create_api()

# Create an instance of Reddit class
reddit = create_reddit_instance()

# Custom Parameters
tw_username = 'peepthispic'
banned_strings = ['My ', ' my ', 'I ', ' OC', ' by me']

# Get up to 10 image urls that meet Twitter standards
def image_urls(sub):
    urls = []
    for submission in reddit.subreddit(sub).top(time_filter='day', limit=10):
        url = submission.url
        title = submission.title
        if url.endswith(('.jpg', '.png', '.jpeg')) and len(title)<280 and (any(substring in title for substring in banned_strings) == False):
            urls.append(url)
    return urls

# Get up to 10 image captions that Twitter standards
def image_titles(sub):
    titles = []
    for submission in reddit.subreddit(sub).top(time_filter='day', limit=10):
        title = submission.title
        url = submission.url
        if url.endswith(('.jpg', '.png', '.jpeg')) and len(title)<280 and (any(substring in title for substring in banned_strings) == False):
            tclean = regex.sub("[\{\(\[].*?[\}\)\]]", "", title)
            titles.append(tclean)
    return titles

# Tweet image with caption
def tweet_image(message, url):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        tweet = api.update_status_with_media(status=message, filename = filename)
        os.remove(filename)
        return tweet
    else:
        print("Unable to download image")

    
# Get a random sub from custom feed and tweet a random image from the approved images
if __name__ == '__main__':
    rand_sub = random.choice(subreddits)
    rand_post = random.randint(0,len(image_urls(rand_sub))-1)
    tweet_image(message=image_titles(rand_sub)[rand_post], url=image_urls(rand_sub)[rand_post])
