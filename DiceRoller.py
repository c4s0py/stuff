import tkinter as tk
import random


#identify the button function
def printinput():
    mod = inputtxt.get('1.0', 'end-1c')
    if mod.isnumeric():
        print("its a number")
        gen = random.randint(1, 20)
        Result.config(text=int(gen) + int(mod))
        print(gen)
    else:
        print("its not a number")
        notnum.config(text= "please input a number.", font="Aerial 10 bold")


#first frame
frame=tk.Tk()
frame.title("Dice Roller")
frame.geometry('400x200')
frame.config(bg="Grey")
frame.iconbitmap("dice.ico")

#dice text
dicetext = tk.Label(text = "Input Modifiers",
                    background = "Grey")
dicetext.pack()

#input box
inputtxt = tk.Text(frame,
                   height = 2,
                   width = 5)
inputtxt.pack()

#roll button
rollbutton = tk.Button(frame,
                       text= "Roll!",
                       command= printinput)
rollbutton.pack()

notnum = tk.Label(text = "", 
                  background= "Grey")
notnum.pack()

Result = tk.Label(frame, text = "", background="grey")
Result.pack()


frame.mainloop()

# Make a simple dice roller that can add modifiers, base is done, just need to workout adding modifiers to finalised value. having trouble adding integers with strings.
# need to figure it put. c:
