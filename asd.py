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
print(f"\n{hdiv} Question 4 {hdiv}")
print("Well, thats Odd.")

user_number_input = EMInput("Give me a number and I'll show you the sum of all of the odd numbers including the maximum value!", "int", "Please enter a number.")

sum = 0
for i in range(1,user_number_input+1): #since we are starting from 1, n + 2 will always result in an odd number. 
    if (i%2) == 1: 
        sum += i 
print(f"The sum of all odd numbers up to {user_number_input} is {sum}")