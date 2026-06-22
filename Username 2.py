'''
date: 22/06/2026
purpose: To create a window with username and password.
Author: Saman
'''
#Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

t = 3

def go():
    global t
    
    u = e1.get()
    p = e2.get()
    
    if u == "admin" and p == "1234":
        msg.config(text="Logged in")
        img_label.config(image=ok)
        tries.config(text="")
    
    else:
        t = t - 1
        
        if t > 0:
            msg.config(text="Wrong")
            tries.config(text="Left: " + str(t))
            img_label.config(image="")
        else:
            msg.config(text="Locked")
            tries.config(text="None")
            img_label.config(image=no)
            btn.config(state="disabled")

#Root window
root = tk.Tk()
root.title("Math quiz")
root.geometry("355x559")
#Background image
bg_image = tk.PhotoImage(file="background 3.png")

#Bg size
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root,text="Username", font=("Sniglet", 30, "bold"), bg="white", fg="#574e99").pack()
e1 = Entry(root)
e1.pack(pady=100)

Label(root,text="Password", font=("Sniglet", 30, "bold"), bg="white", fg="#574e99").pack()
e2 = Entry(root,show="*")
e2.pack(pady=100)

btn = Button(root,text="Login",command=go, font=("Sniglet", 25, "bold"), bg="#e3dfff", fg="#574e99",)
btn.pack(pady=10)

msg = Label(root,text="")
msg.pack()

tries = Label(root,text="")
tries.pack(pady=10)

img_label = Label(root)
img_label.pack(pady=10)

root.mainloop()
