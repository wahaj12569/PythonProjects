from skpy import Skype
from dotenv import load_dotenv
import os
import os.path

load_dotenv()

email = os.getenv('SKYPE_MAIL')
password = os.getenv('SKYPE_PASSWORD')

slogin =Skype(email,password)
# group=slogin.chats.create(['live ides'])

contact = slogin.contacts['Live Id']
with open('path of file','mod'):
    contact.chat.sendFile('path of file','name of file',image=True)

# contact = slogin.contacts['cf0e6215-34fe-409b-9e4b-135d7f3aa13b']
# contact.chat.sendMsg('how are you')
# print('Done')


# for i in contact:
#     print(i)