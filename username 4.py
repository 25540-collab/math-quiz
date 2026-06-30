'''
date: 23/06/2026
purpose: To create a GUI for math quiz, username window.
Author: Saman
'''
# Import tkinter to make GUI
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#username window
def open_login_window():
    login = tk.Tk()
    login.title("Login")
    login.geometry("800x522")
# Background image
    bg_image = tk.PhotoImage(file="background 3.png")
    
# bg size
    bg_label = tk.Label(login, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Exist Button 
    close_btn = tk.Button(login,text="X",font=("coming soon", 10, "bold"),fg="white",bg="#D9534F",width=3,command=login.destroy)
    close_btn.place(x=750, y=20)

# Login
    header = tk.Label(login,text="Login", font=("Sniglet", 50, "bold"), fg="#574e99", bg="white")
    header.pack(pady=55)

# Username label 
    username_label = tk.Label(login,text="Username", font=("Sniglet", 30, "bold"), fg="#574e99",  bg="white" )
    username_label.pack(pady=1)

# Username entry 
    username_entry = tk.Entry(login,font=("coming soon", 14, "bold"),bg="#e6eefd",fg="#3184e1",relief="flat",width=25 )
    username_entry.pack()

# Password label 
    password_label = tk.Label(login,text="Password",font=("Sniglet", 30, "bold"),fg="#574e99", bg="white")
    password_label.pack()

# Password entry
    password_entry = tk.Entry(login, font=("coming soon", 14, "bold"),bg="#e6eefd",fg="#3184e1",relief="flat",width=25,show="•")
    password_entry.pack()

# Login Button
    def login_action():
        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            messagebox.showwarning("Error", "Please enter both fields.")
        else:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            login.destroy()
            
# Login buttton
    login_btn = tk.Button(login,text="Login",font=("Sniglet", 16, "bold"),fg="#cc007e",bg="#ebc4f2",relief="flat",width=12,command=login_action)
    login_btn.pack(pady=10)


    login.mainloop()


# Run 
open_login_window()
