import smtplib as s

ob =s.SMTP("smtp.gmail.com",587)
ob.ehlo()
ob.starttls()

ob.login("wahaj12569@gmail.com",'$rekCAH12569$')
subject="python test1"
body="I love python"
massage="subject:{}\n\n{}".format(subject,body)
list_address=["muhammadahab8055@gmail.com"]
ob.sendmail("wahaj12569@gmail.com",list_address,massage)
print("mail sent!")
ob.quit()