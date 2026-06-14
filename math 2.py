'''
date: 15/06/2026
purpose: To create a GUI for math quiz.
Author: Saman
'''
#Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Root window
root = tk.Tk()
root.title("Math quiz")
root.geometry("800x522")
#Background image
bg_image = tk.PhotoImage(file="background 3.png")

#window label
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#welcome message
welcome_text = tk.Label(root, text="Welcome to math quiz!", font=("Sniglet", 35, "bold"), bg="white", fg="#574e99")
welcome_text.pack(pady=50)

#Are you ready message
ready_text = tk.Label(root, text="Are you ready?", font=("coming soon", 20), bg="white", fg="#574e99")
ready_text.pack(pady=5)

#Buttons to enter quiz
#Username window
def open_username_window():
    username_window = tk.Toplevel(root)
    username_window.geometry("800x522")
    username_window.title("Ussermane Window")
    
#Username label
    tk.Label(username_window, text="Enter your username", font=("coming soon", 20), bg="white", fg="#574e99").pack(pady=20)

#Button placement
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=(0, 20))

#Yes Button
yes_button = tk.Button(root, text="Yes",command=open_username_window,  font=("Sniglet", 30, "bold"), bg="#e3dfff", fg="#574e99",)
yes_button.pack(side=BOTTOM, padx=5)

#Bind open the username window
root.bind('<Return>', lambda event: open_username_window())

#No Button
no_button = tk.Button(root, text="No", command=root.destroy, font=("Sniglet", 30, "bold"), bg="#e3dfff", fg="#574e99",)
no_button.pack(padx=10)

#Bind t exist  the whole quiz 
root.bind('<Escape>', lambda event: root.destroy())


root.mainloop()

