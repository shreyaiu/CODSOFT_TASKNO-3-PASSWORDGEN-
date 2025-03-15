import random
from tkinter import *
window = Tk()

window.title("Random Password Generator")

window.geometry("600x600")

Label(window, font=('bold', 8), text='Generate Password').pack()

length1 = IntVar()
length2 = IntVar()
length3 = IntVar()
length4 = IntVar()
length5 = IntVar()

def passwordGeneration(n):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&_'

    password = ''.join(random.sample(characters, n))

    l.config(text = password) # Update the label with the generated password

def getLength():
    if length1.get() == 1:
        passwordGeneration(4)
    elif length2.get() == 1:
         passwordGeneration(6)
    elif length3.get() == 1:
         passwordGeneration(8)
    elif length4.get() == 1:
         passwordGeneration(10)
    elif length5.get() == 1:
         passwordGeneration(12)

Button(window, text='Generate Password', font=('normal', 10),bg='green', command=getLength).place(x=230, y=100)

Checkbutton(window, text='4 character', variable=length1).place(x=250, y=150)
Checkbutton(window, text='6 character', variable=length2).place(x=250, y=170)
Checkbutton(window, text='8 character', variable=length2).place(x=250, y=190)
Checkbutton(window, text='10 character', variable=length4).place(x=250, y=210)
Checkbutton(window, text='12 character', variable=length5).place(x=250, y=230)

l = Label(window, text='', font=('bold', 15))
l.place(x=225, y=65)

window.mainloop()
    
