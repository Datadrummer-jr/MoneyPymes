from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = os.getenv("API_ID_TELEGRAM")
API_HASH = os.getenv("API_HASH_TELEGRAM")

if __name__ == "__main__":
    pass