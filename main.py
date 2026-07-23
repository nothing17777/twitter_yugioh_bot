import os
import base64
import requests
from nacl import encoding, public

import yugioh, format

CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["REFRESH_TOKEN"]
GH_PAT = os.environ["GH_PAT"]
REPO = os.environ["GITHUB_REPOSITORY"]

def refresh_access_token():
    resp = requests.post(
        "https://api.x.com/2/oauth2/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
        },
        auth=(CLIENT_ID, CLIENT_SECRET),
    )
    resp.raise_for_status()
    return resp.json()

def update_github_secret(name, value):
    key_resp = requests.get(
        f"https://api.github.com/repos/{REPO}/actions/secrets/public-key",
        headers={"Authorization": f"token {GH_PAT}"},
    )
    key_resp.raise_for_status()
    key_data = key_resp.json()

    public_key = public.PublicKey(key_data["key"].encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(value.encode("utf-8"))
    encrypted_b64 = base64.b64encode(encrypted).decode("utf-8")

    requests.put(
        f"https://api.github.com/repos/{REPO}/actions/secrets/{name}",
        headers={"Authorization": f"token {GH_PAT}"},
        json={"encrypted_value": encrypted_b64, "key_id": key_data["key_id"]},
    ).raise_for_status()

def upload_image(access_token, image_path):
    with open(image_path, "rb") as f:
        media_data = base64.b64encode(f.read()).decode("utf-8")

    resp = requests.post(
        "https://api.x.com/2/media/upload",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"media_data": media_data},
    )
    resp.raise_for_status()
    return resp.json()["data"]["id"]

def post_tweet(access_token, text, media_id=None):
    payload = {"text": text}
    if media_id:
        payload["media"] = {"media_ids": [media_id]}
    resp = requests.post(
        "https://api.x.com/2/tweets",
        headers={"Authorization": f"Bearer {access_token}"},
        json=payload,
    )
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    card = yugioh.getRandomCard()
    cardData = yugioh.cleanCardData(card)
    tweetText = format.format_tweet(cardData)
    print(tweetText)

    tokens = refresh_access_token()
    access_token = tokens["access_token"]
    new_refresh_token = tokens.get("refresh_token", REFRESH_TOKEN)

    media_id = None
    image_path = format.download_image(cardData)
    if image_path:
        try:
            media_id = upload_image(access_token, image_path)
        except Exception as e:
            print(f"Error uploading image: {e}")
        finally:
            if os.path.exists(image_path):
                os.remove(image_path)

    result = post_tweet(access_token, tweetText, media_id)
    print("Tweeted!", result)

    if new_refresh_token != REFRESH_TOKEN:
        update_github_secret("REFRESH_TOKEN", new_refresh_token)
