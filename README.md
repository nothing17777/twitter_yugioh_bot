# Yu-Gi-Oh! Twitter Bot 🃏

A simple Python bot that tweets a random Yu-Gi-Oh! card every time you run it. It fetches card data from the YGOProDeck API and posts the card name, type, description, and image to Twitter.

## Prerequisites

- Python 3.8+
- A Twitter Developer Account (with Read and Write permissions)

## Setup

1.  **Clone or Download this folder.**

2.  **Install Dependencies:**
    Open your terminal/command prompt in this folder and run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:**
    - Rename `.env.example` to `.env`.
    - Open `.env` and paste your Twitter API credentials:
        ```env
        API_KEY=...
        API_SECRET=...
        ACCESS_TOKEN=...
        ACCESS_TOKEN_SECRET=...
        ```
    *Note: Ensure your Twitter App has "Read and Write" permissions enabled in the Developer Portal.*

## Usage

To post a new card to Twitter immediately, run:

```bash
python main.py
```

## Project Structure

- `main.py`: The entry point. Coordinates fetching the card and posting the tweet.
- `yugioh.py`: Handles fetching random card data from the API.
- `format.py`: Formats the tweet text and handles image downloading.
- `config.py`: Loads credentials and connects to the Twitter API.
- `cardImages/`: Directory where temporary card images are saved.
