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
Button(root,text="Easy",font=("Sniglet", 28, "bold"),bg="#ddd8ff",fg="#574e99",relief="flat",width=10,cursor="hand2").place(x=300, y=150)

# Medium button
Button(root,text="Medium",font=("Sniglet", 28, "bold"),bg="#ddd8ff", fg="#574e99", relief="flat", width=10,cursor="hand2").place(x=300, y=280)

# Hard button
Button(root,text="Hard",font=("Sniglet", 28, "bold"),bg="#ddd8ff",fg="#574e99",relief="flat",width=10,cursor="hand2").place(x=300, y=370)

# Next button
Button(root,text="➜",font=("Arial", 20, "bold"),bg="#f4b7e6",fg="#d4006d",relief="flat",width=2,height=1,cursor="hand2").place(x=700, y=410)

# Next label
Label(root,text="next",font=("Arial", 16),bg="#f8d7e8",fg="#d4006d").place(x=700, y=470)

root.mainloop()


