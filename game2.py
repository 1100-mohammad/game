#============================= 1
from tkinter import *
import tkinter.messagebox
import random
#============================= 2
root = Tk()

#============================= 3
root.title("rock,paper,scissor")
root.geometry("400x330")
root.resizable(width=False, height=False)
color = "#031cfc"
root.configure(bg = color)


#============================== 4
top_first = Frame(root,width=400,height=50,bg=color)
top_first.pack(side='top')

top_second = Frame(root,width=400,height=50,bg=color)
top_second.pack(side='top')

top_thrid = Frame(root,width=400,height=50,bg=color)
top_thrid.pack(side='top')

top_forth = Frame(root,width=400,height=50,bg=color)
top_forth.pack(side='top')

top_five = Frame(root,width=400,height=50,bg=color)
top_five.pack(side='top')

top_six = Frame(root,width=400,height=50,bg=color)
top_six.pack(side='top')

top_seven = Frame(root,width=400,height=50,bg=color)
top_seven.pack(side='top')

top_eight = Frame(root,width=400,height=50,bg=color)
top_eight.pack(side='top')

#============================== 5
btn_1 = Button(top_second,text="daste chap",width=30,highlightbackground=color,command=lambda: rast())
btn_1.pack(side = LEFT,padx=5,pady=5)

btn_2 = Button(top_first,text="daste rast",width=30,highlightbackground=color,command=lambda: chap())
btn_2.pack(side = LEFT,padx=5,pady=5)

btn_3 = Button(top_forth,text="",width=30,highlightbackground=color)
btn_3.pack(side = LEFT,padx=5,pady=5)

btn_4 = Button(top_six,text="",width=30,highlightbackground=color)
btn_4.pack(side = LEFT,padx=5,pady=5)

btn_5 = Button(top_eight,text="creator",width=20,highlightbackground=color,command=lambda: creator())
btn_5.pack(side = LEFT,padx=5,pady=5)

btn_6 = Button(top_eight,text="clear",width=20,highlightbackground=color,command=lambda: clear())
btn_6.pack(side = LEFT,padx=5,pady=5)


#============================== 6
def rast():
    z = random.randint(0,1)
    if z == 0 :
        btn_3['text']= "gol"
        btn_4['text']= "you win!"
    elif z == 1 :
        btn_3['text']= "pooch"
        btn_4['text']= "you lose!"
        

def chap():
    z = random.randint(0,1)
    if z == 0 :
        btn_3['text']= "gol"
        btn_4['text']= "you win!"
    elif z == 1 :
        btn_3['text']= "pooch"
        btn_4['text']= "you lose!"


def clear():
    btn_3['text']= ""
    btn_4['text']= ""
    

def creator():
    tkinter.messagebox.showinfo("creator", "creat by mohammad sadegh alijani")
#============================== 7
d = Label(top_thrid,text="computer move :",bg=color)
d.pack(side=LEFT,padx=5,pady=5)

g = Label(top_five,text="result :",bg=color)
g.pack(side=LEFT,padx=5,pady=5)


#============================== run
root.mainloop
