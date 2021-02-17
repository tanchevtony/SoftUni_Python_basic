#  this is guess the number game.

import random

name = input("Hello! What is your name?\n")

number = random.randint(0, 20)
print(f"Well, {name} , Let's play.\nI'm thinking of a number between 1 and 20.")
games = int(input("How many guesses you want to make?\n"))

guesses_taken = 0
guess = False

for guesses_taken in range(1, games + 1):
    print("Take a guess.")
    guess = int(input())

    if guess < number:
        print("Your guess is too low")
    elif guess > number:
        print("Your guess is too high")
    else:
        break
if guess != number:
    print(f"Nope. The number I was thinking of was {number}.")
else:
    print(f"Good job, {name}!\nYou guessed my number in {guesses_taken} guesses ")

