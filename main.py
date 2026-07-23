import os
import tempfile

import config, yugioh, format
import requests

if __name__ == "__main__":
    card = yugioh.getRandomCard()
    cardData = yugioh.cleanCardData(card)
    tweetText = format.format_tweet(cardData)
    print(tweetText)

    media_ids = []
    image_url = cardData.get("image") if cardData else None

    if image_url:
        try:
            img_resp = requests.get(image_url, timeout=10)
            img_resp.raise_for_status()
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
                tmp.write(img_resp.content)
                tmp_path = tmp.name

            media = config.v1_api.media_upload(filename=tmp_path)
            media_ids.append(media.media_id)
            os.remove(tmp_path)
        except Exception as e:
            print(f"Error uploading image: {e}")

    if media_ids:
        config.client.create_tweet(text=tweetText, media_ids=media_ids)
    else:
        config.client.create_tweet(text=tweetText)

    print("Tweeted!")
