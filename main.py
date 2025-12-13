import config, yugioh, format
import schedule
import time

if __name__ == "__main__":
    card = yugioh.getRandomCard()
    cardData = yugioh.cleanCardData(card)
    tweetText = format.format_tweet(cardData)
    # Append the image URL to the tweet text so Twitter generates a preview
    #if "image" in cardData:
    #    tweetText += f"\n{cardData['image']}"

    print(tweetText)
    config.client.create_tweet(text=tweetText)
    print("Tweeted!")