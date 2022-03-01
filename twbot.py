
import smtplib
import tweepy
import re
import time

global last_tweet_doge
tweet = ""

def buy(current_tweet):
    global tweet
    print(current_tweet)
    if current_tweet == tweet:
        print("already sent")
        return
    tweet = current_tweet
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    try:
        s.login("-----@gmail.com", "pass_here")
    except:
        print("Error de contacto")
    return

    message = "Account active"
    s.sendmail("------@gmail.com","----@gmail.com" message)
    s.quit()
    
auth = tweepy.OAuthHandler("_____")
auth.set_access_token("_______")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

while(True):
    print("app start")
    user = api.get_user("elonmusk")

    print("User details:")
    print(user.name)
    tweets = api.user_timeline(screen_name="@elonmusk", count = 5, include_rts = False, exclude_replies= True)
    tweets_for_csv = [tweet.text for tweet in tweets]
    print("appp start")
    possible_hints = ["doge", "bitcoin", "eth"]
    for current_tweet in tweets_for_csv:
        current_tweet = current_tweet.lower()
        for hints in possible_hints:
            if re.search(hints, current_tweet):
                buy(current_tweet)
                break

    time.sleep(300)

