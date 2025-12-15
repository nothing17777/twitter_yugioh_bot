import os
import requests
from PIL import Image
from io import BytesIO

# Where we want to save the temporary image
IMAGE_PATH = "cardImages/card.png"

def url_to_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def download_image(card_data):
    """
    Downloads the image from the card data and saves it locally.
    Returns: path to the saved image
    """
    image_url = card_data.get("image")
    if not image_url:
        return None
    
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        # Ensure directory exists
        os.makedirs(os.path.dirname(IMAGE_PATH), exist_ok=True)
        
        image.save(IMAGE_PATH)
        print("done saving image")
        return IMAGE_PATH
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def format_tweet(card_data):
    """
    Takes the clean card dictionary and creates a nice Tweet string.
    Also downloads the image locally.
    Returns: dictionary with 'text' and 'image_path'
    """
    
    # Safety check
    if not card_data:
        return {"text": "Error: No data", "image_path": None}

    # 1. Grab data
    name = card_data["name"]
    card_type = card_data["type"]
    description = card_data["description"]
    
    # 2. Text Formatting
    header = f"🃏 {name}\nType: {card_type}\n\n"
    hashtags = "\n\n#YuGiOh #YuGiOhBot"
    
    tweet_limit = 250 # Reserve space for image URL (23 chars) and standard 280 limit
    reserved_space = len(header) + len(hashtags) + 3
    available_space = tweet_limit - reserved_space
    
    if len(description) > available_space:
        description = description[:available_space] + "..."
        
    tweet_text = f"{header}{description}{hashtags}"

    return tweet_text
if __name__ == "__main__":
    # Test block
    test_card = {
        "name": "Dark Magician",
        "type": "Normal Monster",
        "description": "The ultimate wizard in terms of attack and defense.",
        "image": "https://images.ygoprodeck.com/images/cards/46986414.jpg"
    }
    
    result = format_tweet(test_card)
    print("--- Final Result ---")
    print(result)