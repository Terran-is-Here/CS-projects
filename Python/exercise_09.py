# Exercise #09
# Name Pablo Luis Cauton
# Date 2025-04-07
# This is a program where we practice for loops, random number generators, and counters.

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
# 01 - Use a for loop to print your name 10 times using one print statement inside the loop.
# Have it then print the word “Done” at the end.
print(f"\n{hdiv} Question 1 {hdiv}")
print("10 Names")

for i in range(0,10):
    print("Pablo Luis Cauton")
print("Done")

# 02 - Use a for loop to print two words 7 times all on separate lines using one print statement inside the loop. 
# The second word also needs to be tabbed (HINT: Escape characters)
print(f"\n{hdiv} Question 2 {hdiv}")
print("2 Words, 2 Lines")

for i in range(0,7):
    print("Word1\n\tWord2")
print("Done")


# 03 - Use a for loop to print the even numbers from 2 to 12, inclusive (which means including 2 and 12).
# (HINT: Modulus division - if a number modulus(%) divided by 2 equals 0 then it's an even number.)
print(f"\n{hdiv} Question 3 {hdiv}")
print("Even?")
for i in range(2,13):
    if i % 2 == 0:
        print(i)


# 04 - Use a for loop to print all the numbers between 0 and user inputted number inclusive, going up by 5.
print(f"\n{hdiv} Question 4 {hdiv}")
print("Going up by fives")

user_number = EMInput("Give me a number to count up to (by fives):", "int", "Please give an integer.")
accum = 5
for i in range(0,(user_number+1)):
    if accum == 5:
        print(i)
        accum = 0
    accum += 1 


# 05 - Use a for loop to print all the numbers between 100 and 90 inclusive, going down by one.
print(f"\n{hdiv} Question 5 {hdiv}")
print("Counting Down")

number = 100
for i in range(0,11):
    print(number)
    number -= 1 

# 06 - Use a for loop to ask the user for 5 numbers and count how many are negative.

print(f"\n{hdiv} Question 6 {hdiv}")
print("Counting Down")
number_list = []
negative_numbers = 0
for i in range (0,5):
    user_number = EMInput(f"Give me a number to check the sign of (Number {i+1}/5): ", "float", "Please enter a number.")
    if abs(user_number) != user_number: #checks if the number is negative, in which case |x| != x.
        negative_numbers += 1 
    number_list.append(user_number)
print(f"There were {negative_numbers} negative numbers in the following set: {number_list}")

# 07 - Use a for loop to display 10 random numbers between 1 and 100.
print(f"\n{hdiv} Question 7 {hdiv}")
print("10 Random Numbers")
for i in range(0,10): 
    print(random.randint(1,100))

# 08 - Use a for loop to display a chart like the one on the website.
# Square = i * i, Cube = i * i * i
print(f"\n{hdiv} Question 8 {hdiv}")
print("Powers")
print(hdiv*3)
print("Number\tSquare\tCube")
for i in range(1,11): 
    print(f"{i}\t{i*i}\t{i*i*i}")


# 09 - Use a for loop to display the multiplication equation and answers for the numbers between 20 and 30 inclusive.
print(f"\n{hdiv} Question 9 {hdiv}")
print("Multiplication Tables")
for i_1 in range(20,31):
    for i_2 in range(20,31):
        print(f"{i_1} * {i_2} = {i_1 * i_2}")


# 10 - Generate 1000 random numbers between 1 and 5. 
# Display a chart showing the number of times each number was generated. 
# Use a counter for each number. 
# Counters need to be initialized before they are used. example: count1 = 0
print(f"\n{hdiv} Question 10 {hdiv}")
print("1-5 Randomness Tracker")

values = [0,0,0,0,0] 
for i in range(0,1000):
    number_chosen = random.randint(1,5)
    values[number_chosen-1] += 1
h = 0
for i in values: 
    print(f"{h+1} appeared {i} times")
    h += 1
# 11 - Run a loop 20 times and print out whether the number is odd or even except for numbers 4 and 13 which are unlucky.
print(f"\n{hdiv} Question 11 {hdiv}")
print("Odd or Even Tracker")
unlucky_numbers = [4,13]
for i in range (1,20):
    if i not in unlucky_numbers: 
        match i%2:
            case 1:
                print(f"{i} is odd.")
            case 0:
                print(f"{i} is even.")
