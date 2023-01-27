from datetime import date
from config import create_api
import random
import billboard

api = create_api()

def create_daily_tweet_content():
    today = date.today()
    year = str(int(str(today)[:4]) - random.randint(1,40))
    hot_100 = billboard.ChartData('hot-100', date = year + str(today)[4:])
    content = "Billboard Hot 100 today in " + year + "\n" + "#1 " + str(hot_100[0]) + "\n" + "#2 " + str(hot_100[1]) + "\n" + "#3 " + str(hot_100[2])
    return content


def send_tweet(content):
    tweet = api.update_status(content)
    return tweet


def create_daily_tweet():
    content = create_daily_tweet_content()
    # print generated content to the console
    print(f"Generated tweet: \n{content}")
    # return tweet to get tweet_id for subtweet
    return send_tweet(content)


if __name__ == "__main__":
    create_daily_tweet()
