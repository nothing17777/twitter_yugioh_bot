import config, yugioh, format
import schedule
import time

if __name__ == "__main__":
    card = yugioh.getRandomCard()
    cardData = yugioh.cleanCardData(card)
    tweetText = format.format_tweet(cardData)
    image = format.download_image(cardData)
    media_id = config.api.media_upload(filename=image).media_id_string
    print(media_id)
    print(tweetText)
    config.client.create_tweet(text=tweetText, media_ids=[media_id])
    print("Tweeted!")