import random
import requests
from config import create_api, create_reddit_instance
import os

# Create Twitter API
api = create_api()

# Create an instance of Reddit class
reddit = create_reddit_instance()

def image_urls(sub):
    urls = []
    for submission in reddit.subreddit(sub).hot(limit=10):
        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            urls.append(url)

def image_titles(sub):
    titles = []
    for submission in reddit.subreddit(sub).hot(limit=10):
        title = submission.title
        titles.append(title)

def tweet_image(url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_status_with_media(status=message, filename = filename)
        os.remove(filename)
    else:
        print("Unable to download image")

if __name__ == '__main__':
    random_number = random.randint(0,9)
    tweet_image(url=image_urls()[random_number], message=image_titles()[random_number])
