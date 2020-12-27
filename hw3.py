# Sibel Akayoğlu
# HW3 - HANGMAN GAME

import os

secret_word = "globalaihub"
guesses = ''
turnover = 10
os.system("cls")

user_name = input("What is your name? ")

while turnover > 0: 
    os.system("cls")
    print("Welcome {}\nLets play hangman\n".format(user_name))      
    failed = 0 

    for char in secret_word:      
        if char in guesses:    
            print(char)
        else:
            print("_")    
            failed += 1    

    if failed == 0:        
        print("\nYou won !!!")
        break              

    print()
    guess = input("guess a character:") 
    guesses += guess                    

    if guess not in secret_word:  
        turnover -= 1
        print("Wrong")
        print("Wrong answer!\nYou have {} more guesses".format(turnover))
        input()
        if turnover == 0:
            print("\nYou Lose")  
            input()