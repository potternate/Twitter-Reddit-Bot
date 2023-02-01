import random
import requests
from config import create_api, create_reddit_instance
import os

# Subreddit 
subreddit = 'rareinsults'

# Create Twitter API
api = create_api()

# Create an instance of Reddit class
reddit = create_reddit_instance()

def image_urls(sub):
    urls = []
    for submission in reddit.subreddit(sub).hot(limit=15):
        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            urls.append(url)
    return urls

def image_titles(sub):
    titles = []
    for submission in reddit.subreddit(sub).hot(limit=15):
        title = submission.title
        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            titles.append(title)
    return titles

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

if __name__ == '__main__':
    random_number = random.randint(0,len(image_urls()))
    tweet_image(message=image_titles(subreddit)[random_number], url=image_urls(subreddit)[random_number])
