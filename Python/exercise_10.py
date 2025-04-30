# Exercise #10
# Name Pablo Luis Cauton    
# Date 2025-04-10
# This is a program where we practice for loops, accumulators, and counters.

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
# 01 - Write a program that asks for 5 integers and calculate their sum using a for loop.
print(f"\n{hdiv} Question 1 {hdiv}")
print("Sigma Notation")
print("Give me 5 numbers and I shall calculate their sum!")
values = []
total_value = 0
for i in range(0,5): 
    values.append(EMInput(f"Number ({i+1}/5): ", "float", "Please enter a number."))
    total_value += values[i]
print(f"Values inputted: {values}, Total sum: {total_value} ")

# 02 - Using a for loop, write a program that asks a user to enter whether they won (W) or lost (L) each of their last ten games.
# Assume there were no ties.
# Output to the user the total number of wins and the total number of losses.
print(f"\n{hdiv} Question 2 {hdiv}")
print("Ws or Ls")
print("Tell me if you won (or not) your last 10 games.")
record = []
number_of_games_to_record = 10
totals = [0, 0]
states = ["W", "L"]
for i in range(0,number_of_games_to_record):
    while True: 
        state = EMInput(f"Game #{i+1} (W/L?): ", "str","Please enter in text.")
        if state.upper() not in states: 
            print("Please enter W for Wins, and L for Losses.")
        else:
            break
    if state.upper() == "W":
        record.append(state.upper())
        totals[0] += 1
    elif state.upper() == "L":
        record.append(state.upper())
        totals[1] += 1
    else: 
        print("What did you do?")
    
print(f"Game Record: {record}\n Total Wins: {totals[0]}\n Total Losses: {totals[1]}")


# 03 - Using a for loop, write a program that asks a user how many items were on their grocery bill.
# Then ask the user to enter the cost of each item on the grocery bill.
# When the user is done, output the hst and the total cost of their groceries.
print(f"\n{hdiv} Question 3 {hdiv}")
print("Cost Calculator")
number_of_items = EMInput("How many items did you buy for your groceries today?", "int", "Please enter an integer value.")
subtotal = 0
for i in range(0,number_of_items): 
    subtotal += EMInput(f"How much did item #{i+1} cost?: ", "float", "Please enter a number.")
print(hdiv*2)
print(f"Subtotal: {subtotal:.2f}$")
print(f"HST (13%): {(subtotal*0.13):.2f}$")
print(f"Total: {(subtotal*1.13):.2f}$")
# 04 - Using a for loop, write a program that asks for a number of marks, collects them, and computes the average.
print(f"\n{hdiv} Question 4 {hdiv}")
print("Mark Average Calculator")
subjects = []
subject_marks = []
total = 0
amount_of_subjects = EMInput("How many grades / subjects are we taking the average of today?: ", "int", "Please enter an integer number.")
for i in range(0,amount_of_subjects): 
    subjects.append(EMInput(f"What is subject #{i+1}?:  ", "str"))
    subject_marks.append(EMInput(f"What is your mark in {subjects[i]} (Subject #{i+1}): ", "float", "Enter a number please."))
    total += subject_marks[i]
if amount_of_subjects == 0:
    amount_of_subjects = 1 # for debugging
average = total / amount_of_subjects
for i in subjects: 
    index = subjects.index(i)
    print(f"{i} (Subject #{index + 1}): {subject_marks[index]}")
print(f"Grade Average: {average}")

# 05 - Using a for loop, write a program to display all the numbers divisible by the user entered number between 1 and 100.
print(f"\n{hdiv} Question 5 {hdiv}")
print("Divisibility Calculator")
number_range = 100
print(f"Give me a number to see what numbers in the range of 1 - {number_range} (inclusive) can be divided by it.")

while True: 
    number=  EMInput("Your Number: ", "int", "Please enter an integer.")
    
    if number != 0 and not number > 100: 
        break
    print("Please enter a non-zero number, or a number within the acutal range.")
divisble_numbers = []

for i in range(1,number_range+1): 
    if (i%number) == 0:
        divisble_numbers.append(i)
print(f"Numbers that {number} can cleanly divide:")
print(divisble_numbers)


# 06 - Read two positive integers, m and n, and print a rectangle of stars using a for loop.
# For example, if m=5 and n=8 then your program should display the rectangle below.
print(f"\n{hdiv} Question 6 {hdiv}")
print("Star Rectangle")
width = EMInput("Please give me a number as to how many asterisks wide this rectangle should be: ", "int", "Please enter a number.")
height = EMInput("Please give me a number as to how many asterisks tall this rectangle should be: ", "int", "Please enter a number.")
for i in range(0,height): 
    print("*"*width)
# ********
# ********
# ********
# ********
# ********