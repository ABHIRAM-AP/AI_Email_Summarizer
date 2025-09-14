import os,requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_API')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def send_summary_to_telegram(msg:str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id":CHAT_ID,"text":msg}
    requests.post(url,data=data)