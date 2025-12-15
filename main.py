import config, yugioh, format
import schedule
import time

if __name__ == "__main__":
    card = yugioh.getRandomCard()
    cardData = yugioh.cleanCardData(card)
    tweetText = format.format_tweet(cardData)
    print(tweetText)
    config.client.create_tweet(text=tweetText)
    print("Tweeted!")