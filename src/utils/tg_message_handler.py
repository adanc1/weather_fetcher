import requests
from decouple import config

def send_message(message):
    url = f"https://api.telegram.org/bot{config('TG_BOT_TOKEN')}/sendMessage"
    payload = {
        "chat_id": config("CHAT_ID"),
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    print(response.json())
