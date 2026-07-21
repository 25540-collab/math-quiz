'''
date: 13/07/2026
purpose: To create a window with levels.
Author: Saman
'''
# Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Functions
# New window called easy level
def easy_window():
    easy = Toplevel(root)
    easy.title("Easy level")
    easy.geometry("400x300")
    Label(easy, text="Easy level", font=("Sniglet", 24)).pack(pady=100)
# New window called medium level
def medium_window():
    medium = Toplevel(root)
    medium.title("Medium level")
    medium.geometry("400x300")
    Label(medium, text="Medium level", font=("Sniglet", 24)).pack(pady=100)
# New window called hard level
def hard_window():
    hard = Toplevel(root)
    hard.title("Hard level")
    hard.geometry("400x300")
    Label(hard, text="Hard Quiz", font=("Sniglet", 24)).pack(pady=100)

# Level window
root = Tk()
root.title("Choose Level")
root.geometry("800x522")

# Background image
bg_image = tk.PhotoImage(file="background 3.png")
# bg size
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Choose level message
start_text = tk.Label(root, text="Choose level", font=("Coming soon", 50, "bold"), bg="white", fg="#574e99")
start_text.pack(pady=60)

# Easy button
Button(root,text="Easy",command=easy_window,font=("Sniglet", 28,"bold"),bg="#ddd8ff",fg="#574e99",relief="flat",width=10,cursor="hand2").place(x=300, y=150)

# Medium button
Button(root,text="Medium",command=medium_window,font=("Sniglet", 28, "bold"),bg="#ddd8ff",fg="#574e99",relief="flat",width=10,cursor="hand2").place(x=300, y=280)

# Hard button
Button(root, text="Hard", command=hard_window, font=("Sniglet", 28, "bold"), bg="#ddd8ff", fg="#574e99", relief="flat", width=10, cursor="hand2").place(x=300, y=370)

root.mainloop()
