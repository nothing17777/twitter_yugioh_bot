""" 
Important: yugioh.py returns card data, not tweet text.
🎯 Goal of yugioh.py
By the end, yugioh.py should be able to:
1. Fetch one random Yu-Gi-Oh card
2. Clean and normalize the data
3. Hand back something safe and predictable to the rest of your bot
"""
import requests
import json

# Function to fetch a random Yu-Gi-Oh card
def getRandomCard():
    url = "https://db.ygoprodeck.com/api/v7/randomcard.php"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("Request successful")
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching random card: {e}")
        return None

# Function to clean and normalize card data
def cleanCardData(card):
    if not isinstance(card, dict):
        print("Invalid card data")
        return None

    cardData = card["data"][0]
    if not cardData:
        print("Invalid card data")
        return None

    cardName = cardData["name"]
    cardType = cardData["type"]
    cardDescription = cardData["desc"]
    cardImage = cardData["card_images"][0]["image_url"]

    if not cardName or not cardType or not cardDescription or not cardImage:
        print("Invalid inner card data")
        return None

    return {
        "name": cardName,
        "type": cardType,
        "description": cardDescription,
        "image": cardImage
    }



if __name__ == "__main__":
    print(cleanCardData(getRandomCard()))
