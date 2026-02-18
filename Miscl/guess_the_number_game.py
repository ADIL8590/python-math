import numpy as np
print("Welcome to the guess the number game.You have Eleven attempts to guess the number between 1 and 100.")
number=int(input("Enter your number:"))
number_to_guess=np.random.randint(1,100)
attempts=11
while attempts>0:
    if number==number_to_guess:
        print("Congratulations! You guessed the number correctly.")
        break
    elif number<number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts-=1
    if attempts>0:
        print(f"number of attempts left: {attempts}")
        number=int(input("Enter your number:"))
    
if attempts==0:
    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
    print("Better luck next time!, Thank you for playing the game.")
