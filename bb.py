from datetime import date
from config import create_api
import random
import billboard

api = create_api()

def create_daily_tweet_content():
    today = date.today()
    year = str(int(str(today)[:4]) - random.randint(1,40))
    which_chart = random.randint(0,7)
    
    if which_chart == 0:
        if int(year) > 2014:
            artist = billboard.ChartData('artist-100', date = year + str(today)[4:])
            content = "Billboard Artist 100 today in " + year + "\n" + "#1 " + str(artist[0]) + "\n" + "#2 " + str(artist[1]) + "\n" + "#3 " + str(artist[2])
        else:
            which_chart = random.randint(1,7)
    elif which_chart == 1:
        if int(year) > 2012:
            streaming = billboard.ChartData('streaming-songs', date = year + str(today)[4:])
            content = "Top Streaming Songs today in " + year + "\n" + "#1 " + str(streaming[0]) + "\n" + "#2 " + str(streaming[1]) + "\n" + "#3 " + str(streaming[2])
        else:
            which_chart = random.randint(2,7)
    elif which_chart == 2:
        if int(year) > 1991:
            radio = billboard.ChartData('top-album-sales', date = year + str(today)[4:])
            content = "Top Radio Songs today in " + year + "\n" + "#1 " + str(radio[0]) + "\n" + "#2 " + str(radio[1]) + "\n" + "#3 " + str(radio[2])
        else:
            which_chart = random.randint(4,7)        
    elif which_chart == 3:
        if int(year) > 1991:
            album = billboard.ChartData('top-album-sales', date = year + str(today)[4:])
            content = "Top Album Sales today in " + year + "\n" + "#1 " + str(album[0]) + "\n" + "#2 " + str(album[1]) + "\n" + "#3 " + str(album[2])
        else:
            which_chart = random.randint(4,7) 
    elif which_chart == 4:
        country = billboard.ChartData('country-songs', date = year + str(today)[4:])
        content = "Top Country Songs today in " + year + "\n" + "#1 " + str(country[0]) + "\n" + "#2 " + str(country[1]) + "\n" + "#3 " + str(country[2])
    elif which_chart == 5:
        pop = billboard.ChartData('pop-songs', date = year + str(today)[4:])
        content = "Top Pop Songs today in " + year + "\n" + "#1 " + str(pop[0]) + "\n" + "#2 " + str(pop[1]) + "\n" + "#3 " + str(pop[2])
    elif which_chart == 6:
        rbhiphop = billboard.ChartData('r-b-hip-hop-songs', date = year + str(today)[4:])
        content = "Top R&B/Hip-Hop Songs today in " + year + "\n" + "#1 " + str(rbhiphop[0]) + "\n" + "#2 " + str(rbhiphop[1]) + "\n" + "#3 " + str(rbhiphop[2])
    elif which_chart == 7:
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
