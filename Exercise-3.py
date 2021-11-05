import random

x = random.randint(0,50)
guess = int(input("Enter your guess"))
while(guess != x):
    if(guess>x):
        print("Decrease your guess")
        guess = int(input("Enter your guess "))
    elif(guess<x):
        print("Inrease your guess")
        guess = int(input("Enter your guess "))
print("Your guess", guess," is correct")