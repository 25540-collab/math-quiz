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


# Functions
# Questions
#Decimals -> percentages 
questions = [
    {"question": "Convert 0.4 to a percentage.", "answer": "40%"},
    {"question": "Convert 0.72 to a percentage.", "answer": "72%"},
    {"question": "Convert 0.02 to a percentage.", "answer": "2%"},
    {"question": "Convert 0.8 to a percentage", "answer": "80%"}

]
current = 0
score = 0

# load question
def load_question():
    question_label.config(text=questions[current]["question"])
    qnum_label.config(text=f"{current+1}/{len(questions)}")
    answer.delete(0, tk.END)

# Submit
def submit():
    global score

    if answer.get() == questions[current]["answer"]:
        score += 1

    score_label.config(text=f"{score}\nscore")
    messagebox.showinfo("Answer", "Answer submitted!")

#Next question
def next_question():
    global current

    if current < len(questions) - 1:
        current += 1
        load_question()
    else:
        messagebox.showinfo("Finished", f"You scored {score}/{len(questions)}")

# Previous question
def previous_question():
    global current

    if current > 0:
        current -= 1
        load_question()
        
# Hint function
def hint():
    ans = questions[current]["answer"]
    messagebox.showinfo("Hint", f"The answer starts with {ans[0]}")

# Score
score_label = tk.Label(root,text="0\nscore",fg="#cc007e",bg="#f4e2d5",font=("Arial", 10))
score_label.place(x=650, y=10)

# Question number
qnum_label = tk.Label(root, text="1/3\nQ num", fg="#cc007e", bg="#f4e2d5", font=("Arial", 10))
qnum_label.place(x=720, y=10)

# Placeholder for image
image_label = tk.Label(root,text="Image related to the\nquestion",width=18,height=4,bg="#DDEEFF")
image_label.pack()

# Question
question_label = tk.Label(root,text="",font=("Arial", 18),bg="white")
question_label.pack(pady=10)

# Answer box
answer = tk.Entry(root, font=("Arial", 16), justify="center", width=10)
answer.pack()

# Submit button
submit_btn = tk.Button(root,text="Submit answer",command=submit,bg="#E6D9FF",fg="#cc007e")
submit_btn.pack(pady=10)

# Bottom buttons
bottom = tk.Frame(root, bg="#574e99")
bottom.pack(side="bottom", fill="x", pady=15)

# Timer
timer = tk.Label(bottom,text="00:00:00",fg="#cc007e",bg="#f4e2d5")
timer.pack(side="left", padx=10)

# Hint button
hint_btn = tk.Button(bottom,text="Hint",command=hint,bg="#3A66A7",fg="#78abe4")
hint_btn.pack(side="left")

# Back button
back_btn = tk.Button(bottom,text="<-", command=previous_question,bg="#F3B6E5",fg="#cc007e", font=("Arial", 12, "bold"))
back_btn.pack(side="right", padx=5)

# Next button
next_btn = tk.Button( bottom,text="->",command=next_question,bg="#F3B6E5",fg="#cc007e",font=("Arial", 12, "bold"))
next_btn.pack(side="right", padx=5)

load_question()

root.mainloop()
