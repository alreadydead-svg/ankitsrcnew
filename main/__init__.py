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
SESSION = "BQCCMEIYm9IGh27K44oui0t2dBC7KW9YhzFXNNIwF7bGdsdUikJpZSRbosz_ku85a0FfFC04pzPtTYRK-8jT_GLKK5nD2udJlyUj364Mazmw1q5eYqAKiJCbMZz2C79SU1-bCnQLOqMUd49ZHQLdEHk93bB4alL54j6Ru0sahlRxbZOgev1lBp2BRfP7Bhz3ene8CdjbWBu7id3vfGUhb2bUR4Wh_3esA-iWbb7dgQ4AORgMYE-8fFF1SsqN8yyULg_TWgem0okcTYpmEYmFZQX3F7IRyWXqV_DlphmjHxuKINn0SnTDt_Wmh0qEdIwomgOJo81A9iUrDQvLrCMj6w31QmDlxAA"
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
