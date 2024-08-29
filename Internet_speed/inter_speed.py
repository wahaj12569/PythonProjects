from tkinter import *
import speedtest

def speedcheck():
    sp =speedtest.Speedtest()
    sp.get_servers()
    down =str(round(sp.download()/(10**6),3))+"Mbps"
    up =str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_download.config(text=down) 
    lab_upload.config(text=up)

sp = Tk()
sp.title('Internet Speed Tester')
sp.geometry('500x650')
sp.config(bg='steelblue')

lab=Label(sp,text='Internet speed test',font=('Time New Roman',30,"bold"),bg='skyblue',fg='black')
lab.place(x=110,y=40)

lab=Label(sp,text='Downloading speed!',font=('Time New Roman',30,"bold"),bg='skyblue',fg='black')
lab.place(x=60,y=130,height=50,width=380)
lab_download=Label(sp,text='00',font=('Time New Roman',30,"bold"),bg='skyblue',fg='black')
lab_download.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text='Uploading speed!',font=('Time New Roman',30,"bold"),bg='skyblue',fg='black')
lab.place(x=60,y=290,height=50,width=380)
lab_upload=Label(sp,text='00',font=('Time New Roman',30,"bold"),bg='skyblue',fg='black')
lab_upload.place(x=60,y=360,height=50,width=380)

button =Button(sp,text='Check speed',font=('Time New Roman',30,"bold"),relief=RAISED,command=speedcheck)
button.place(x=60,y=460,height=50,width=380)


sp.mainloop()