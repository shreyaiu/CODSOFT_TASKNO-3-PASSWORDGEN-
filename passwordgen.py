# A password generator is a useful tool that generates strong and random passwords for users.
# This project aims to create a password generator application using python, allowing users to specify the length and complexity of the password.
# User Input:R\Prompt the user to specify the desired length of the password.
# Generate password:Use a combination of random characters to generate a password of the specified length.
# Display the password: Print the generated password on the screen.

import random
from tkinter import *

# Creating a window
window = Tk()

# Providing the title of the window
window.title("Random Password Generator")

# Setting the size of the window
window.geometry("600x600")

# Adding a label
Label(window, font=('bold', 8), text='Generate Password').pack()

# Variables to store checkbox values
length1 = IntVar()
length2 = IntVar()
length3 = IntVar()
length4 = IntVar()
length5 = IntVar()

# Function to generate random password
def passwordGeneration(n):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&_'

    # Generating random password ans strong it
    password = ''.join(random.sample(characters, n))

    #update the label with the generated password
    l.config(text = password) # Update the label with the generated password

# GetLength function will call the passwordGeneration function
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

# Creating buttons
Button(window, text='Generate Password', font=('normal', 10),bg='green', command=getLength).place(x=230, y=100)

# Creating Checkboxes
Checkbutton(window, text='4 character', variable=length1).place(x=250, y=150)
Checkbutton(window, text='6 character', variable=length2).place(x=250, y=170)
Checkbutton(window, text='8 character', variable=length2).place(x=250, y=190)
Checkbutton(window, text='10 character', variable=length4).place(x=250, y=210)
Checkbutton(window, text='12 character', variable=length5).place(x=250, y=230)

# Label to display the generated password
l = Label(window, text='', font=('bold', 15))
l.place(x=225, y=65)

window.mainloop()
    