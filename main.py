# Guessing the Number!!
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f"Guess a Numer between 1 to {x} "))
        if(guess < random_number):
            print(f"Sorry, Guess Again, Too Low!! ")
        elif(guess > random_number):
            print(f"Sorry, Guess Again, Too High!! ")
        
    print(f"yay, Congrats. You have Guessed the Number {random_number} Correctly!!")

x = int(input("Enter a Number you want to play Between!! "))
guess(x)
    