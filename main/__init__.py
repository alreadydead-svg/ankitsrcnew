#Github.com/mrinvisible7

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26075120"
API_HASH = "1fda88a5d1de46058a4791c78bce198e"
BOT_TOKEN = "6686507792:AAGandOVJTw_41Z3EMkKhKfLu4XQhQ9BOBc"
SESSION = "BQGTAMIAcSu2DsQ9iX545imfMwJqIE50PUIVPVkZKv3UpGx9C689yAZ_GSmbSFmZOmQPpJ4CUBIGdr65F0YFy2QVFNfSkcd_aNadGFmnhQSyJkeKED4YAJvQIEZHgBFkxFwbJ8akcYV49dMOMgi_C42rwny4ZXqpY0hmTeO3DA8NhdhLUzUnrLWEWxH3nLXBQIi__1xbq9jQ4KnGtxHNzfffMuGe-uuyiGhyl6yLkN0jKjyxZomNAop-QBf35VPqV0Ez6qexQwO4m8aCYC_DiH4xVw2wEVQ41Abp6zC4dIDWf7jItTaNXa0foT0CiWxdSbG59TM6xQrGculuj3alaJtQ0y-hNAAAAAGGgvMwAA"
FORCESUB = "stringsessionAK47"
AUTH = "6551696176"
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
