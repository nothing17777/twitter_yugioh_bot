import os
import tweepy
from dotenv import load_dotenv

# 1. Load the passwords from the .env file
load_dotenv()

# 2. Assign them to python variables
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# 3. Connect to Twitter (OAuth 2.0)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)    

# 4. Set up the authentication (OAuth 2.0)
auth = tweepy.OAuth2BearerHandler(bearer_token)
api = tweepy.API(auth)