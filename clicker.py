import tkinter as tk
import keyboard as kb 
import pyautogui as pya


base = tk.Tk()
base.title("C4's Clicker")
base.geometry("250x150")
base.resizable(False, False)

title = tk.Label(text="C4's Clicker",
                 font=("arial", 15))
                 
title.pack()


x = 0
b = 0

def roll():
    global x
    x += 1
    print("Clicked", x , "times")
    counter.config(text=x)

def toggle():
    global b
    b ^= 1
    if b == 1:
        print("Toggled ON")
        while b == 1:
            pya.click()
            warning.config(text="Warning! Autoclicker is active")
            if kb.is_pressed("f1"):
                break
    if b == 0:
        print("Toggled OFF")
        warning.config(text="")

kb.add_hotkey("f1", toggle)

button = tk.Button(base,
                   text="Test",
                   width="5",
                   height="3",
                   command=roll)
button.pack()

warning = tk.Label(base,
                  text="",
                  fg="red",)

warning.pack()

counter = tk.Label(base,
                  text="") 

counter.pack()

togglekey = tk.Label(base,
                  text="Press F1 to toggle the autoclicker",
                  font=("arial", 7)) 

togglekey.place(x=55, y=130)


bottom = tk.Label(text="ver. 1.0",
                 font=("arial", 7),
                 )
                 
bottom.place(x=5, y=135)

base.mainloop()