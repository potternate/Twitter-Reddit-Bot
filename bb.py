from datetime import date
from config import create_api
import random
import billboard

api = create_api()

def create_daily_tweet_content():
    today = date.today()
    year = str(int(str(today)[:4]) - random.randint(1,40))
    which_chart = random.randint(0,4)
    
    if which_chart == 0:
        hot_100 = billboard.ChartData('hot-100', date = year + str(today)[4:])
        content = "Billboard Hot 100 today in " + year + "\n" + "#1 " + str(hot_100[0]) + "\n" + "#2 " + str(hot_100[1]) + "\n" + "#3 " + str(hot_100[2])
    elif which_chart == 1:
        radio = billboard.ChartData('radio-songs', date = year + str(today)[4:])
        content = "Top Radio songs today in " + year + "\n" + "#1 " + str(radio[0]) + "\n" + "#2 " + str(radio[1]) + "\n" + "#3 " + str(radio[2])
    elif which_chart == 2:
        country = billboard.ChartData('country-songs', date = year + str(today)[4:])
        content = "Top Country songs today in " + year + "\n" + "#1 " + str(country[0]) + "\n" + "#2 " + str(country[1]) + "\n" + "#3 " + str(country[2])
    elif which_chart == 3:
        pop = billboard.ChartData('pop-songs', date = year + str(today)[4:])
        content = "Top Pop songs today in " + year + "\n" + "#1 " + str(pop[0]) + "\n" + "#2 " + str(pop[1]) + "\n" + "#3 " + str(pop[2])
    elif which_chart == 4:
        rbhiphop = billboard.ChartData('r-b-hip-hop-songs', date = year + str(today)[4:])
        content = "Top R&B/Hip-Hop songs today in " + year + "\n" + "#1 " + str(rbhiphop[0]) + "\n" + "#2 " + str(rbhiphop[1]) + "\n" + "#3 " + str(rbhiphop[2])
                        
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
