from instabot import Bot
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('INSTA_ID')
password1 = os.getenv('INSTA_PASSWORD')

bot=Bot()
bot.login(username=email,password=password1)
# bot.follow("wscubetechindia")
# bot.upload_photo("/Users/mini/Downloads/Amazon-Logo-31.png",caption="congratulations!") 
# bot.unfollow("wscubetechindia")
# bot.send_message("kasa ha? nafay!",['wahajlatif_official'])
# followers =bot.get_user_followers("itach_i5747")
# for follower in followers:
#     print(bot.get_user_info(follower))

