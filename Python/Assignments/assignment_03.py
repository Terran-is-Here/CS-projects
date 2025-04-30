# Assignment #03
# Name Pablo Luis Cauton
# Date 2025-04-15
# Cumulative Task

#same old EMInput module
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
# 01 - Display the numbers 1 through 20 using a for loop.
print(f"\n{hdiv} Question 1 {hdiv}")
print("Counting")
for i in range(1,21):
    print (i)

# 02 - Display all the odd positive integers less than 50 using a for loop with a step.
print(f"\n{hdiv} Question 2 {hdiv}")
print("Odd Counting")
for i in range(50,-1,-1):
    if i % 2 == 1: #modulo checks for oddness; if so then passes it to bottom
        print(i)

# 03 - Print your name to the screen n times, as determined by the user using a for loop.
print(f"\n{hdiv} Question 3 {hdiv}")
print("Not to name names")
Username = EMInput("What is your name?: ")
repeat_times = EMInput(f"How many times do you want me to print out your name {Username}?: ", "int", "Please enter a number.")
for i in range(0,repeat_times): #simple for loop
    print(Username)

# 04 - Given a positive integer n, simulate a countdown from n to 1, followed by the message Blast off using a for loop!
print(f"\n{hdiv} Question 4 {hdiv}")
print("Counting Down")

time = EMInput("From what number are we starting the countdown from?: ", "int", "Please enter a number.")
for i in range(time, -1, -1): #counts down to 0 inclusive; then prints off blastoff!
    print(f"T-Minus: {i}")
print("Blast Off!")

# 05 - Display all integers between m and up to an including n, with step s, as determined by the user using a for loop.
print(f"\n{hdiv} Question 5 {hdiv}")
print("Ooh, Numbers")
class numbers: #basic class for grouping these things up.
    lower_bound = EMInput("What is the lower bound of numbers you want to display?\n Input:", "int", "Please enter a number.")
    upper_bound = EMInput("What is the upper bound of numbers you want to display? (inlusive)\n Input:", "int", "Please enter a number.")
    step = EMInput("What is the step per every message displayed that you want to have?\n Input:", "int", "Please enter a number.")
#general upper bound changes based on the step; due to us needing to increment by one to prevent an off-by-one error.
if numbers.step == 0:
    numbers.step = 1 #edge case handling, since range() with three parameters requires the increment >=1.
    numbers.upper_bound = numbers.upper_bound + 1
elif numbers.step < 0:
    numbers.upper_bound = numbers.upper_bound - 1
else: 
    numbers.upper_bound= numbers.upper_bound + 1
for i in range(numbers.lower_bound, numbers.upper_bound, numbers.step): #range with these values already includes off-by-one error correction
    print(i)

# 06 - Using a for loop, output an addition table for whichever numbers the user requests.
# For example, if the user enters 5 and 10, your output should be:
# 5 + 5 = 10
# 6 + 6 = 12
# ...
# 10 + 10 = 20
print(f"\n{hdiv} Question 6 {hdiv}")
print("As simple as addition.")
print("Enter two numbers for me to create an addition table for you!")

n1 = EMInput("Number 1: ", "int","Please enter an integer number.")
n2 = EMInput("Number 2: ", "int","Please enter an integer number.")

for i in range(n1, n2+1): #iterates through every first number..
    for j in range(n1, n2+1): #then iterates through every second number..
        print(f"{i} + {j} = {i + j}") #then displays and calculates their sum. 