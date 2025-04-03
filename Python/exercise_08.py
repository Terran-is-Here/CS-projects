# Exercise #08
# Name (fill in your name)
# Date (fill in the date)
# This is a program where we practice if statements, random number generators, and counters.

import random
import sys 
hdiv = "="*10
def EMInput(input_string, return_type ="str", error_message = "Error in input. Please try again."): #error-managed input v1.3?, removed formatting since directly passing f-strings is now the practice.
    while True:
        try: 
            inputted_value = eval(f"{return_type}(input(input_string))")
        except KeyboardInterrupt: 
            print("\nExiting program due to KeyboardInterrupt.")
            sys.exit() #re-implements forced exit on Ctrl+C KeyboardInterrupt errors.
        except ValueError: 
            print(error_message) # will handle type-matching errors, like inputting a string to a int()
        else:
            return inputted_value
    
# 01 - Create a program that simulates a coin flip.
print(f"\n{hdiv} Question 1 {hdiv}")
print("Heads or Tails")

coin_states = ["heads", "tails"]
while True: 
    print("I am about to flip a coin, please enter your guess if it will land heads or tails.")
    while True:
        guess = EMInput("Type your Guess: ", "str")
        if guess.lower() not in coin_states: 
            print(f"Please enter heads or tails.")
        else:
            break

    coin_flip_result = random.randint(0,1)

    if guess.lower() == coin_states[coin_flip_result].lower(): 
        print(f"Congratulations, the coin rolled {coin_states[coin_flip_result]}, and your guess was {guess}!")
    else:
        print(f"A shame, the coin rolled {coin_states[coin_flip_result]}, and your guess was {guess} :( ")
    if EMInput("Do you still want to continue playing? \n(Enter Yes to continue, else this will continue to the next question): ", "str").lower() != "yes": 
        break
    
# 02 - Create a program that simulates the rolling of a die. If the user gets a 2 or a 4, they win.
print(f"\n{hdiv} Question 2 {hdiv}")
print("Rolling the dice of fate")


class user: 
    winning_states = [2,4] #set of winning numbers
    score = 0 
while True:
    user.score = 0 
    dice_results = []

    print(f"This is a rolling die game. A dice needs to roll a number within this set: {user.winning_states} to win.")
    while True: 
        number_of_rolls = EMInput("How many dice do you want to roll?: ", "int", "Please enter a non-decimal integer.")
        if number_of_rolls > 0: 
            break
        else:
            print(f"Please enter a number greater than 0.")
    for i in range(0,number_of_rolls): #iterates through lists
        dice_results.append(random.randint(1,6))
        if dice_results[i] in user.winning_states: 
            user.score += 1 
    print(f"Your score is {user.score}. \n These were the following dice roll results: {dice_results}.")
    if EMInput("Do you still want to continue playing? \n(Enter Yes to continue, else this will continue to the next question): ", "str").lower() != "yes": 
        break

# 03 - Create a program that simulates the rolling of two separate dice. If the user gets a pair, they win.
print(f"\n{hdiv} Question 3 {hdiv}")
print("Two Dice is better than one")
print("Another RNG game; I shall roll two dice and see if they equal eachother\nif they do, you WIN!")
while True: 
    dice_results = [random.randint(1,6),random.randint(1,6)] #reusing variable since Q2 code is no logner executed
    if dice_results[0] == dice_results[1]: 
        print(f"Congratulations, both dice rolled the same number: \nDice 1 rolled {dice_results[0]}\nDice 2 rolled {dice_results[1]}")
    else:
        print(f"Sorry, both dice did not roll the same number: \nDice 1 rolled {dice_results[0]}\nDice 2 rolled {dice_results[1]}")
    if EMInput("Do you still want to continue playing? \n(Enter Yes to continue, else this will continue to the next question): ", "str").lower() != "yes": 
        break

# 04 - Create a simple guessing game program where the computer generates a number between 1-10
# The user gets one chance to guess the number.
print(f"\n{hdiv} Question 4 {hdiv}")
import math
print("Guess The Number")
print("The rules of the game are simple: guess the number that the RNG machine in this computer came up with.")
    
while True:
    difficulty = EMInput("Do you want to play the easy version of this game, or the hard one?\n(Easy or Hard input):")
    if difficulty.lower() == "hard":
        #equivalent to sin(a)*4bc*10^d rounded to 10 decimal points, floating point imprecision is our key
        computer_guess = round(random.random()*4*random.random()*math.pow(10,random.random())*math.sin(random.random()),10)
    else:
        computer_guess = random.randint(1,6)

    guess = EMInput("This computer has already come up with a number, please enter what number do you think it is?\nYour Guess:")
    if difficulty.lower() == "hard":
        if guess == computer_guess: 
            print("Im.. genuinely impressed, you guessed the same number as the computer. What the hell?")
        else: 
            print(f"This difficulty is quite rigged, sorry that you got it wrong :p.\nComputer Guess: {computer_guess}\nYour Guess:{guess}")
    else: 
        if guess == computer_guess: 
            print("Congratulations, you guessed the name number as the computer!")
        else: 
            print(f"This difficulty is quite fair unlike hard mode, sorry that you got it wrong :p.\nComputer Guess: {computer_guess}\nYour Guess:{guess}")
    if EMInput("Do you still want to continue playing? \n(Enter Yes to continue, else this will continue to the next question): ", "str").lower() != "yes": 
        break

# 05 - Create a simple rock, paper, scissors program where the computer generates a random choice of rock, paper, or scissors.
print(f"\n{hdiv} Question 5 {hdiv}")
print("Rock Paper Scissors")
options = ["rock", "paper", "scissors"]

# Below is a possibility table for Rock, Paper, Scissors.  
# Rows are for the choices that the computer chooses, as such the player choice is a subset of the row, that is
# possibilities[computer choice][player choice]
# Each Row / Column is defined in the order of Rock, Paper and Scissors. 
# A value of 0 indicates that the computer wins. A value of 1 indicates the player wins
# A value of 2 indicates a tie. 
possibilities = [
    [2,1,0],
    [0,2,1],
    [1,0,2],
]
print("You will be going up against my great computer-scissor-rock-inator-thingy! Pick between rock, paper and scissors to defeat it.")
while True: 
    computer_choice = random.randint(0,2)
    while True:
        user_choice = EMInput("Choose between rock, paper and scissors: ")
        if user_choice.lower() not in options: 
            print("Please pick one of the three choices please")
        else:
            break
    result = possibilities[computer_choice][options.index(user_choice.lower())]
    if result == 0:
        print(F"The computer won! You chose {user_choice}, the computer chose {options[computer_choice]}")
    elif result == 1:
        print(F"You won! You chose {user_choice}, the computer chose {options[computer_choice]}")
    elif result == 2:
        print(F"Its a tie. You chose {user_choice}, the computer chose {options[computer_choice]}\n")
    if EMInput("Do you still want to continue playing? \n(Enter Yes to continue, else this will continue to the next question): ", "str").lower() != "yes": break
