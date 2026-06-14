import tkinter as tk

def open_next_window():
    # Create the new window
    next_window = tk.Toplevel(root)
    next_window.geometry("300x200")
    next_window.title("Next Window")
    
    # Add elements to the new window
    tk.Label(next_window, text="Welcome to the next window!").pack(pady=20)

#Main window setup
root = tk.Tk()
root.geometry("300x200")
root.title("Main Window")

#Yes Button
yes_button = tk.Button(root, text="Yes", command=open_next_window)
yes_button.pack(pady=20)

#open the next window
root.bind('<Return>', lambda event: open_next_window())

#No Button - Closes the window when clicked
no_button = tk.Button(root, text="No", command=root.destroy)
no_button.pack(pady=10)

#Exist window
root.bind('<Escape>', lambda event: root.destroy())


root.mainloop()
