import smtplib as s
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('SMTP_EMAIL')
password = os.getenv('SMTP_PASSWORD')

ob =s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()

ob.login(email,password)
subject="python test1"
body="I love python"
massage="subject:{}\n\n{}".format(subject,body)
list_address=["muhammadahab8055@gmail.com"]
ob.sendmail("wahaj12569@gmail.com",list_address,massage)
print("mail sent!")
ob.quit()