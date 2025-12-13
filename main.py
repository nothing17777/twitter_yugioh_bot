import config, yugioh

if __name__ == "__main__":
    card = yugioh.getRandomCard()
    cardData = yugioh.cleanCardData(card)
    config.client.create_tweet(text=cardData["description"])