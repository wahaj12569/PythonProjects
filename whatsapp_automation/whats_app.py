import pywhatkit as pyw 
from dotenv import load_dotenv
import os

load_dotenv()
num =os.getenv('WHATSAPP_NUM')

pyw.sendwhatmsg(num,'It is testing',7,26)