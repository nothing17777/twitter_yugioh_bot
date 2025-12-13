import config
import sys

print("--- Authentication Debugger ---")

# 1. Check if keys are loaded
keys = {
    "API_KEY": config.api_key,
    "API_SECRET": config.api_secret,
    "ACCESS_TOKEN": config.access_token,
    "ACCESS_SECRET": config.access_token_secret
}

missing = [k for k, v in keys.items() if not v]
if missing:
    print(f"❌ Error: The following keys are missing in .env or config.py: {missing}")
    sys.exit(1)

print("✅ generic check: All 4 keys are present.")

# 2. Check Key formats (Basic heuristic)
if len(config.api_key) < 15:
    print("⚠️ Warning: Your API_KEY looks too short. Are you sure it's the Consumer Key?")

if not config.access_token.startswith("1") and "-" not in config.access_token:
    print("⚠️ Warning: Your ACCESS_TOKEN usually starts with numbers and a dash (e.g., '12345-abcde'). Check if you pasted the right one.")

# 3. Test Connection
print("\nAttempting to connect to Twitter...")
try:
    user = config.api.verify_credentials()
    if user:
        print(f"✅ Success! Authenticated as @{user.screen_name}")
    else:
        print("❌ Failed: verify_credentials returned None")
except Exception as e:
    print(f"❌ Authentication Failed: {e}")
    print("\nPossible solutions:")
    print("1. Did you Regenerate your API Key/Secret as well? If so, update those too.")
    print("2. Make sure you don't have extra spaces in your .env file.")
