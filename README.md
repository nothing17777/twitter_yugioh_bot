# 🃏 Yu-Gi-Oh! Twitter Bot

A lightweight Python bot that summons a random **Yu-Gi-Oh!** card and tweets it to the world. It automatically fetches card details and artwork from the [YGOProDeck API](https://db.ygoprodeck.com/api-guide/) and posts them to your Twitter account.

---

## 📋 Prerequisites

Before you start, ensure you have the following:

*   **Python 3.8** or higher installed.
*   A **Twitter Developer Account** with an App created.
*   **"Read and Write"** permissions enabled for your Twitter App.

---

## 🚀 Setup Guide

### 1. Clone the Repository
Download the project code to your local machine:
```bash
git clone https://github.com/nothing17777/twitter_yugioh_bot.git
cd twitter_yugioh_bot
```

### 2. Install Dependencies
Install the required Python libraries using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Configure Credentials
The bot needs your Twitter API keys to work.

1.  Rename the example environment file:
    ```bash
    mv .env.example .env
    ```
2.  Open `.env` in a text editor and paste your credentials:
    ```env
    API_KEY=your_consumer_key_here
    API_SECRET=your_consumer_secret_here
    ACCESS_TOKEN=your_access_token_here
    ACCESS_TOKEN_SECRET=your_access_token_secret
    ```

> **⚠️ Important:** Make sure your keys allow **Write** access. If you get a 403 error, check your Twitter Developer Dashboard settings and regenerate your Access Tokens.

---

## ⚔️ Usage

To summon a card (run the bot manually), simply execute:

```bash
python main.py
```

The bot will:
1.  Fetch a random card.
2.  Download the card image locally.
3.  Upload the image and tweet the card details.
4.  Print the Tweet URL or status to the console.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `main.py` | **Entry Point**. Orchestrates the fetching and tweeting process. |
| `config.py` | Handles Twitter authentication and API connection. |
| `yugioh.py` | Wrapper for the YGOProDeck API to fetch card data. |
| `format.py` | Formats the tweet text and handles image downloading/resizing. |
| `cardImages/` | Directory for temporary image storage. |
| `.env` | **Secret**. Stores your API keys (Ignored by Git). |

---

## 🔗 Credits

*   Card Data & Images provided by the [YGOProDeck API](https://db.ygoprodeck.com/api-guide/).
*   Twitter integration via [Tweepy](https://www.tweepy.org/).

---

*“It’s time to Duel!”*
