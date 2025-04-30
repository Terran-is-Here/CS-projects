# Exercise #12
# Name Pablo Luis Cauton
# Date 2025-04-23
# This is a program where we practice loops, counters and accumulators

import random
import sys 
hdiv = "="*10
def EMInput(input_string, return_type ="str", error_message = "Error in input. Please try again."):
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
        
# 01 - Write a program that asks for the user to enter a word and have the computer print out that word until 
# the user types in "stop copying me" which then prints out a final statement.
print(f"\n{hdiv} Question 1 {hdiv}")
print("Copycat")

user_input = EMInput("Give me a word and I'll keep on copying it until you beg me to stop!")
while True: 
    print(user_input)
    if EMInput("User Input Needed:").lower() != "stop copying me": 
        print(f"Wrong, :p, {user_input}")
    else:
        print("Alright, fine I'll stop.")
        break

# 02 - Write a program that asks the user how many lines of emojis they want. Show the amount of emojis on 
# each line you are printing, example on line 4, show 4 emojis. Then have the process reverse.
# To print an emoji - print("\U0001f600")
print(f"\n{hdiv} Question 2 {hdiv}")
print("Emojical Notations")
user_input = EMInput("How many lines of emojis do you want?", "int", "Please enter a whole number.")
emoji = "\U0001f600"
for i in range(0,user_input): 
    print(emoji*(i+1))
for i in range(user_input,0,-1): 
    print(emoji*i)


# 03 - Have the computer generate random numbers between 1 and 31 until the computer guesses your birthday.
print(f"\n{hdiv} Question 3 {hdiv}")
print("Whoops, Forgot your birthday")
class user_info: 
    BMonth= ""
    BDay = 0
    LYear = False

while True: 
    ly_buffer = EMInput("Were you born on a leap year? (y/n / Yes/No): ")
    if ly_buffer.lower() == "yes" or ly_buffer.lower() == "y":
        user_info.LYear = True;break
    elif ly_buffer.lower() == "no" or ly_buffer.lower() == "n":
        user_info.LYear = False;break
    else:
        print("Please enter Yes or No.")

while True:
    user_info.BMonth = EMInput("What month were you born in?")
    if user_info.BMonth.lower() in ["january","february","march","april","may","june","july","august","september","october","november","december"]: break
    print("Please enter an actual month.")

if user_info.BMonth.lower() in ['january', 'march', 'may','july','august','october','december']:
    upperbound = 31
elif user_info.BMonth.lower() in ['april','june','september','november']:
    upperbound = 30
elif user_info.BMonth.lower() == "february":
    if user_info.LYear == True: 
        upperbound = 29
    else:
        upperbound = 28


counter = 0
guessing = True
while guessing: 
    counter += 1 
    guess = random.randrange(1,upperbound+1)
    while True:
        validation = EMInput(f"Is your birthday on {guess}th of {user_info.BMonth}?\n(Yes/No): ", "str").lower()
        if validation == 'yes':
            guessing = False
            break
        else:
            print("Oh, I'll try again then.")
            break

print(f"It took me {counter} attempts to guess your birthday!")

# 04 - Write a program that displays the sum of all of the odd numbers from 1 to a maximum value entered by the user.	 
print(f"\n{hdiv} Question 4 {hdiv}")
print("Well, thats Odd.")

user_number_input = EMInput("Give me a number and I'll show you the sum of all of the odd numbers including the maximum value!", "int", "Please enter a number.")

sum = 0
for i in range(1,user_number_input+1): #since we are starting from 1, n + 2 will always result in an odd number. 
    if (i%2) == 1: 
        sum += i 
print(f"The sum of all odd numbers up to {user_number_input} is {sum}")

# 05 - Write a program that will display the sum of all of the numbers between two values entered by the user. 
# The program should also display an expression showing what specific numbers were summed.
print(f"\n{hdiv} Question 5 {hdiv}")
print("Sigma Notation #2")

print("Give me the two bounds for a function that will add up the nummbers from the lower bound to the upper bound (inclusive):")
lower_bound = EMInput("(Lower Bound): ", "int", "Please enter a number.")
upper_bound = EMInput("(Upper Bound): ", "int", "Please enter a number.")
sum = 0
string_buffer = str(lower_bound)
for i in range(lower_bound, upper_bound+1): #offset by one to make the loop only add a + i per interation)
    sum += i
    string_buffer = string_buffer+ "+" + str(i)
print(f"{string_buffer} = {sum}")

# 06 - Write a program that will help the user to analyze their bowling scores. 
# The user can enter as many scores as they like, entering -1 when they are done entering scores. 
# Your program will then display the highest, lowest, and average scores entered. 
print(f"\n{hdiv} Question 6 {hdiv}")
print("Strike!")

print("Enter Scores for me to calculate things!\nEnter -1 to exit this tool. ")
i = 1
class data: 
    scores = [EMInput(f"Score #{i}: ", "int", "Please enter a whole number.")] #assigns the first dummy value prematurely
    high_score = scores[0] #value above prematurely passed into max/min values to populate it.
    low_score = scores[0]

sum = data.scores[0]
while True: 
    i += 1 
    user_input = EMInput(f"Score #{i}: ", "int", "Please enter a whole number.")
    if user_input != -1: 
        data.scores.append(user_input)
        sum += user_input
        if user_input > data.high_score:
            data.high_score = user_input
        if user_input > data.low_score:
            data.low_score = user_input
    else:
        break
print(hdiv*3)
print(f"Scores: {data.scores}")
print(f"High Score: {data.high_score}")
print(f"Low Score: {data.low_score}")
print(f"Average: {(sum/len(data.scores)):,.2f}")


