import random

print("Number Guessing Game")
print("Guess a number between 1-9")
number = random.randint(1,9)
chances = 5
while chances > 0:
    userGuess = int(input("Enter your guess"))
    if(userGuess == number):
        print("CONGRATULATIONS YOU WON !!!")
        break
    elif userGuess > number:
        print("Your guess was too high, Guess a number lower than ",userGuess)
    elif userGuess < number:
        print("Your guess was too low, Guess a number higher than ",userGuess)
    chances = chances-1
if chances == 0:
    print("YOU LOSE, THE NUMBER WAS ",number)