import config
import tweepy

print("--- Rate Limit & Permission Checker ---")

try:
    # 1. Check v1.1 Credentials (just to be safe)
    me = config.api.verify_credentials()
    print(f"✅ Authentication OK. Logged in as: @{me.screen_name}")
except Exception as e:
    print(f"❌ authentication failed: {e}")

try:
    # 2. Try to get v2 limits (This often fails on Free tier, but worth a shot)
    # We try to fetch the logged-in user's own details
    print("Checking v2 Client connectivity...")
    me_v2 = config.client.get_me()
    print(f"✅ v2 Client OK. User ID: {me_v2.data.id}")
    
except tweepy.errors.Forbidden as e:
    print(f"❌ v2 Permission Error: {e}")
    print("This confirms your Access Keys do not have the right permissions OR the App is not in a Project.")
except Exception as e:
    print(f"❌ v2 Error: {e}")

print("\n--- TEST TWEET ---")
try:
    print("Attempting to post a simple test tweet...")
    # Using a timestamp to ensure it's not a duplicate
    import time
    resp = config.client.create_tweet(text=f"Test tweet {time.time()}")
    print(f"✅ SUCCESS! Tweet ID: {resp.data['id']}")
except tweepy.errors.Forbidden as e:
    print(f"❌ 403 FORBIDDEN: {e}")
    # Inspect the API headers if available
    if e.response is not None:
        print("\nAPI Response Headers:")
        for k, v in e.response.headers.items():
            if "limit" in k.lower():
                print(f"{k}: {v}")
    
    print("\nDIAGNOSIS:")
    print("If you see 'x-rate-limit-remaining: 0', you are out of tweets for the day.")
    print("If you don't see headers, checking your Developer Portal 'User Authentication Settings' is the only way.")
    
except Exception as e:
    print(f"❌ Error: {e}")
