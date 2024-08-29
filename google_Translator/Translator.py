from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text ='type',src ='English',dest ='Urdu'):
    text1=text
    src1 =src
    dest1 =dest
    trans = Translator()
    trans1= trans.translate(text=text1,src=src1,dest=dest1)
    return trans1.text

def data():
    s =comb1_sor.get()
    d = comb1_dest.get()
    masg = sor_txt.get(1.0,END)
    textget = change(text=masg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()

root.title('Translator')
root.geometry('1500x800')
root.config(bg='Black')
lable_txt=Label(root,text='Translator',font=('Time New Roman',40,"bold"),bg='Black')
lable_txt.place(x=600,y=40,height=80,width=200)

frame = Frame(root).pack(side=BOTTOM)

lable_txt=Label(root,text='Source Text',font=('Time New Roman',20,"bold"),bg='Black')
lable_txt.place(x=200,y=160,height=40,width=120)
sor_txt = Text(frame,font=('Time New Roman',10,'bold'),wrap=WORD)
sor_txt.place(x=200,y=200,height=200,width=500)

list_text = list(LANGUAGES.values())
comb1_sor =ttk.Combobox(frame,values=list_text)
comb1_sor.place(x=330,y=170,height=30,width=100)
comb1_sor.set('English')

button_change =Button(frame,text='Translate',relief=RAISED,command=data)
button_change.place(x=600,y=400,height=40,width=200)

dest_txt = Text(frame,font=('Time New Roman',10,'bold'),wrap=WORD)
dest_txt.place(x=700,y=200,height=200,width=500)


lable_txt=Label(root,text='Destination Text',font=('Time New Roman',20,"bold"),bg='Black')
lable_txt.place(x=700,y=160,height=40,width=160)
comb1_dest =ttk.Combobox(frame,values=list_text)
comb1_dest.place(x=870,y=170,height=30,width=100)
comb1_dest.set('English')

root.mainloop()