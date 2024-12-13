import random
import time

def main():
    word = random.choice(open("GAME1/words.txt").read().split())
    secret = ['_'] * len(word)
    running = True
    wrong = 6
    guessed_letters = []

    while running:
        print(secret)
        print("You have ", wrong, "/ 6 guesses remaining")
        inpt = input("Make a guess: ").lower()

        if len(inpt) != 1 or not inpt.isalpha():
            print("Invalid Input")
            continue

        if inpt in guessed_letters:
            print(f"{inpt} already guessed.")

        guessed_letters.append(inpt)

        if inpt in word:
            for i in range(len(word)):
                if word[i] == inpt:
                    secret[i] = inpt
        else:
            wrong -= 1
        
        if '_' not in secret:
            print("You win")
            print(word)
            running = False
        elif wrong == 0:
            print("LOSE")
            print("Correct word: " , word)
            running = False

def menu():
    print('''   
 /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$
| $$  | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$
| $$  | $$| $$  \ $$| $$$$| $$| $$  \__/| $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$
| $$__  $$| $$__  $$| $$  $$$$| $$|_  $$| $$  $$$| $$| $$__  $$| $$  $$$$
| $$  | $$| $$  | $$| $$\  $$$| $$  \ $$| $$\  $ | $$| $$  | $$| $$\  $$$
| $$  | $$| $$  | $$| $$ \  $$|  $$$$$$/| $$ \/  | $$| $$  | $$| $$ \  $$
|__/  |__/|__/  |__/|__/  \__/ \______/ |__/     |__/|__/  |__/|__/  \__/                                                                     
    ''')
    time.sleep(2)
    if input("Welcome to hangman, would you like to play? Y/N: ") == "y":
        main()
    else:
        print("OKAY, GOODBYE.")
menu()
            