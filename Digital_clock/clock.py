from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi =time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    month =time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')

    lable_hr.config(text=hr)
    lable_min.config(text=mi)
    lable_sec.config(text=sec)
    lable_am.config(text=am)
    lable_date.config(text=date)
    lable_month.config(text=month)
    lable_year.config(text=year)
    lable_day.config(text=day)
    lable_hr.after(200,date_time)

clock =Tk()
clock.title('Digital Clock')
clock.geometry('1000x500')
clock.config(bg='white')

lable_hr=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_hr.place(x=120,y=50,height=110,width=100)
lable_hr_text=Label(clock,text='HOURS',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_hr_text.place(x=120,y=190,height=40,width=100)

lable_min=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_min.place(x=340,y=50,height=110,width=100)
lable_min_text=Label(clock,text='MINUTES',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_min_text.place(x=340,y=190,height=40,width=100)

lable_sec=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_sec.place(x=560,y=50,height=110,width=100)
lable_sec_text=Label(clock,text='SECONDS',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_sec_text.place(x=560,y=190,height=40,width=100)

lable_am=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_am.place(x=780,y=50,height=110,width=100)
lable_am_text=Label(clock,text='AM/PM',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_am_text.place(x=780,y=190,height=40,width=100)

lable_date=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_date.place(x=120,y=270,height=110,width=100)
lable_date_text=Label(clock,text='DATE',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_date_text.place(x=120,y=410,height=40,width=100)

lable_month=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_month.place(x=340,y=270,height=110,width=100)
lable_month_text=Label(clock,text='MONTH',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_month_text.place(x=340,y=410,height=40,width=100)

lable_year=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_year.place(x=560,y=270,height=110,width=100)
lable_year_text=Label(clock,text='YEAR',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_year_text.place(x=560,y=410,height=40,width=100)

lable_day=Label(clock,text='00',font=('Time New Roman',40,"bold"),bg='yellow',fg='Black')
lable_day.place(x=780,y=270,height=110,width=100)
lable_day_text=Label(clock,text='DAY',font=('Time New Roman',20,"bold"),bg='yellow',fg='Black')
lable_day_text.place(x=780,y=410,height=40,width=100)


date_time()


clock.mainloop()