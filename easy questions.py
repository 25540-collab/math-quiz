'''
date: 22/07/2026
purpose: To create a window with easy questions.
Author: Saman
'''
# Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# easy questions window
root = Tk()
root.title("Easy Level")
root.geometry("800x522")

# Background image
bg_image = tk.PhotoImage(file="background 3.png")
# bg size
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Choose level message
start_text = tk.Label(root, text="Easy level", font=("Coming soon", 50, "bold"), bg="white", fg="#574e99")
start_text.pack(pady=60)

# Next button
Button(root,text="➜",font=("Coming soon", 20, "bold"),bg="#f4b7e6",fg="#d4006d",relief="flat",width=2,height=1,cursor="hand2").place(x=700, y=410)

