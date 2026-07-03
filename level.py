'''
date: 3/07/2026
purpose: To create a GUI for math quiz, level window.
Author: Saman
'''
# Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Root window.
root = tk.Tk()
root.title("Level")
root.geometry("800x522")
# Background image.
bg_image = tk.PhotoImage(file="background 3.png")

# Bg size.
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Choose level message.
start_text = tk.Label(root, text="Choose level", font=("Sniglet", 50, "bold"), bg="white", fg="#574e99")
start_text.pack(pady=60)
