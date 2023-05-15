from tkinter import *
import random

root= Tk()

root.geometry("800x600")

root.title("Find the Ball")

cup_with_ball = 1 + random.randint(0, 2)

# setting the foundation

def reset_game():
    global l1
    global l2
    global cup_with_ball
    global b1
    global b2
    global b3
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    cup_with_ball = 1 + random.randint(0, 2)
    l1.config(text="Click the cup that has the ball")
    l2.config(text="")

def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

frame = Frame(root)
frame.pack()

# define cups

def is_cup(c_v):
    global cup_with_ball
    global l2
    if (c_v == cup_with_ball):
        match_result = "You have found the ball!"
    else:
        match_result = "Sorry, the cup was in cup " + str(cup_with_ball)
    l2.config(text=match_result)
    button_disable()

# defines labels, frames, and buttons

l1 = Label(frame,
    text="Press the cup that has the ball",
    font=10)

l1.pack(side=LEFT)

l2 = Label(root,
    text="",
    font="normal 20 bold",
    bg="white",
    width=35,
    borderwidth=2,
    relief="solid")
l2.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Cup 1",
    font=10, width=7,
    command=lambda: is_cup(1))

b2 = Button(frame1, text="Cup 2",
    font=10, width=7,
    command=lambda: is_cup(2))

b3 = Button(frame1, text="Cup 3",
    font=10, width=7,
    command=lambda: is_cup(3))

Button(root, text="Reset Game",
    font=10, fg="red",
    bg="black", command=reset_game).pack(pady=20)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

root.mainloop()
