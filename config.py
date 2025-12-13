import os
import tweepy
from dotenv import load_dotenv

# 1. Load the passwords from the .env file
load_dotenv()

# 2. Assign them to python variables and STRIP whitespace
bearer_token = os.getenv("BEARER_TOKEN", "").strip()
api_key = os.getenv("API_KEY", "").strip()
api_secret = os.getenv("API_SECRET", "").strip()
access_token = os.getenv("ACCESS_TOKEN", "").strip()
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET", "").strip()

# 3. Connect to Twitter Client (v2)
# NOTE: We removed bearer_token here. For posting Tweets (User Context), 
# we only need the consumer keys and access tokens.
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)    

# 4. Set up the authentication for API (v1.1)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)