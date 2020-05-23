import wolframalpha
import wikipedia
from tkinter import *

def wolf_search(query):
    try:
        global my_query
        my_query=query.lower()
        app_id = 'VLKT3H-GWWK8HYR69'           #get it from wolframeAlpha site
        cleint = wolframalpha.Client(app_id)
        answer = cleint.query(my_query)
        res = next(answer.results).text
        print(res)

    except:
        res = wikipedia.summary(my_query, sentences=2)
        print("according to wikipedia "+ res)
    global Ans
    Ans = Label(frame1, text=res, font=('arial', 15), fg='cyan', bg='gray14',wraplength=500)
    Ans.grid(row=4, column=0,columnspan=3)

def ask_again():
    global Ans
    if Ans['text']!=None:
        Ans['text']=''

win=Tk()
win.config(bg='black')
win.title('Question Bank')

label=Label(win)
label.pack()

frame1=Frame(label,relief=SUNKEN,bg="gray15",bd=10)
frame1.pack()

Title=Label(frame1,text='Ask Me Anything',font=('arial',25,'bold'),fg='green2',bg='gray14').grid(row=1,columnspan=3)

Ask=Label(frame1,text='Ask ',font=('arial',15,'bold'),fg='cyan',bg='gray14').grid(row=2,column=0)

ask_bar = Entry(frame1,bg='black',fg='cyan',font=('arial',15,'bold'),relief=SUNKEN,bd=10)
ask_bar.grid(row=2,column=1,columnspan=2)

find_btn= Button(frame1,text='Find ',bd=5,fg='white',bg='black',font=('arial',20,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:wolf_search(ask_bar.get()))
find_btn.grid(row=3,column=1,sticky='W')

Ask_btn= Button(frame1,text='Ask Again ',bd=5,fg='white',bg='black',font=('arial',20,'bold'),relief=SUNKEN,padx=8,pady=8,command=lambda:ask_again())
Ask_btn.grid(row=3,column=2,sticky='E')

win.mainloop()

