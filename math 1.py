'''
date: 12/06/2026
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
root.geometry("600x800")
#Background image
bg_image = tk.PhotoImage(file="background 2.png")

#window label
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#welcome message
welcome_text = tk.Label(root, text="Welcome to math quiz!", font=("Arial", 24), bg="white")
welcome_text.pack(pady=50)

root.mainloop()
