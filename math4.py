'''
date: 22/06/2026
purpose: To create a GUI for math quiz.
Author: Saman
'''
# Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Root window.
root = tk.Tk()
root.title("Math quiz")
root.geometry("800x522")
# Background image.
bg_image = tk.PhotoImage(file="background 3.png")

# Bg size.
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Sart message.
start_text = tk.Label(root, text="Start", font=("Sniglet", 50, "bold"), bg="white", fg="#574e99")
start_text.pack(pady=60)

# Are you ready message.
ready_text = tk.Label(root, text="Are you ready?", font=("coming soon", 25), bg="white", fg="#574e99")
ready_text.pack(pady=5)

# Buttons to enter quiz.
# Username window.
def open_username_window():
    username_window = tk.Toplevel(root)
    username_window.title("Ussermane Window")
    username_window.geometry("455x659")
    # Bg image
    bg_image = tk.PhotoImage(file="background 4.png")
    # Bg size.
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    
# Username label.
Label(open_username_window,text="Username", font=("Sniglet", 30, "bold"), bg="white", fg="#574e99").pack()
e1 = Entry(open_username_window)
e1.pack(pady=60)

Label(open_username_window,text="Password", font=("Sniglet", 30, "bold"), bg="white", fg="#574e99").pack()
e2 = Entry(open_username_window,show="*")
e2.pack(pady=70)

# Button placement.
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=(0, 20))

# Yes Button.
yes_button = tk.Button(root, text="Yes",command=open_username_window,  font=("Sniglet", 30, "bold"), bg="#e3dfff", fg="#574e99",)
yes_button.pack(side=BOTTOM, padx=5)

# Bind open the username window.
root.bind('<Return>', lambda event: open_username_window())

# No Button.
no_button = tk.Button(root, text="No", command=root.destroy, font=("Sniglet", 30, "bold"), bg="#e3dfff", fg="#574e99",)
no_button.pack(padx=10)

# Bind to exist  the whole quiz. 
root.bind('<Escape>', lambda event: root.destroy())


root.mainloop()

