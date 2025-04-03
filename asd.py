import sys
import math
import random
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