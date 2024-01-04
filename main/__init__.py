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
BOT_TOKEN = "6744432160:AAGzPmaS3J1K35GMnCJAPn_iOFZJXX62kfk"
SESSION = "BQBRvfaMWg1Pdcs-8jtlveRd066_EN4FLshpyoooB603zVycpr2Zm20mJmayW8FlFzrwu-4hBosBLmFBZxQvhAswjlDP4EKLYyW2z-EiCSeAj_VPs6lNwjPkeznT1pANX7OzMyPfLzFK4gbUKJm-eA1ZG7cr6l08GaCLVxUyN1d05ipQIRGgP8iAf_1e5UCDd_0W2McVSwSU8A7qpSw-pIMaTY8iyJ6FOiUo7A9gRMpwevGAMZE-Enwhc6nlL7Y1flHDU17cIJYX9nCSSyd6Fq4yyAVNPAAiNByGmjH_7lFva2HXB9xUtEd-tDl4NOJLxdFohyatDLkO7SL4tviiidH5QmDlxAA"
FORCESUB = "stringsessionAK47"
AUTH = "5903200477"
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
