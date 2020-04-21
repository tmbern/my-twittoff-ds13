# web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", auth) #> <tweepy.auth.OAuthHandler object at 0x110887290>

api = tweepy.API(auth)
print("API", api) #> <tweepy.api.API object at 0x110899790>
print(dir(api))

user = api.get_user("elonmusk")
print("USER", user) #> <class 'tweepy.models.User'>
print(user.screen_name)
print(user.name)
print(user.followers_count)
pprint(user._json)

statuses = api.user_timeline("elonmusk")
pprint(statuses[0]._json)