# Exercise #13
# Name Pablo Luis Cauton
# Date 2025-4-28
# This is a program where we practice try/except
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
        

# 01 - Write a program that adds up all the numbers from 1 to the number you enter and validates the user input.
print(f"\n{hdiv} Question 1 {hdiv}")
print("Errors in the Numbers?")
print("Sigma notation function which given a user input x, adds up all numbers to x: 1 + 2 + ... + x ")
sum = 0
while True: 
    user_input = EMInput("Enter a number:", "int", "Please enter a number. ")
    if user_input <= 0: 
        print("Please enter a positive number greater than one.")
    else:
        break
string_buffer = "1"
sum = 1 #offset due to the way i had the string setup
for i in range(2, user_input+1): #taken from exercise 12 
    sum += i
    string_buffer = string_buffer+ "+" + str(i)
print(f"{string_buffer} = {sum}")

# 02 - Write a program that asks a user to enter their marks. When the user is done entering marks, they will enter -1. 
# The program will calculate the average and validate the user input.
print(f"\n{hdiv} Question 2 {hdiv}")
print("Marking Averages")

marks = []
counter = 1 
sum = 0
while True:

    while True: 
        user_input = EMInput(f"(Input #{counter}): ", "float", "Please enter a valid number.")
        valid_input = True
        if user_input == -1.0:
            print("Exiting loop.")
            valid_input = False
            break
        elif user_input <= 100 and user_input >= 1: break
        else:
            print("Please actually enter a number inbetween 1-100.")
            valid_input = False
            break
    if valid_input ==True:
        counter += 1
        marks.append(user_input)
        sum += user_input
    if user_input == -1: 
        break
try: 
    print(f"Entered Values: \n{marks}\n\nAverage: {sum/len(marks)}")
except ZeroDivisionError: 
    print("No values were given, so no average was calculated.")
            
# 03 - Write a program that asks a user to enter a temperature in celsius. When the user is done entering temps, they will enter "Done". 
# The program will calculate the average temperature (rounded to two decimal places) and validate the user input.
print(f"\n{hdiv} Question 3 {hdiv}")
print("Temperature Averages")
print("Enter temperatures in degC and I shall calculate their average!")


temperatures = []
counter = 1 
sum = 0
while True:
    break_outer_loop = False
    while True: 
        user_input = EMInput(f"Enter a number between 1-100 \n(Input #{counter}): ", "str")
        try: 
            user_input = float(user_input)
            break
        except: 
            if user_input.lower() == "done": 
                print("Temperature calculatior closed.")
                break_outer_loop = True
                break
            else:
                print("Please enter a valid number or the word 'done'. " )
    if break_outer_loop: 
        break
    counter += 1
    temperatures.append(user_input)
    sum += user_input
try: 
    print(f"Entered Values: \n{temperatures}\n\nAverage: {sum/len(temperatures):,.2f}")
except ZeroDivisionError: 
    print("No values were given, so no average was calculated.")