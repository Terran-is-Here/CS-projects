# Exercise #11
# Name (fill in your name)
# Date (fill in the date)
# This is a program where we practice while loops, random number generators, and counters.
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

# 01 - Given a positive integer n, simulate a countdown from n to 1, followed by the message Blast off using a while loop!
print(f"\n{hdiv} Question 1 {hdiv}")
print("Countdown")
n = 10 #countdown
while n > 0: 
    print(f"T-{n}")
    n -= 1 
print("Rocket was launched!")


# 02 - Create a while loop that checks for a number between 1 and 10
print(f"\n{hdiv} Question 2 {hdiv}")
print("IN THE RANGE")

while True: 
    number = EMInput("Enter a number between 1-10, and I'll see if it actually is in there.", "float", "Please enter a number.")
    if number >= 1 and number <= 10: 
        break
    print(f"{number} is not between 1 and 10.")
print(f"{number} was inbetween 1 - 10!")
# 03 - Repeatedly ask the user for a number using a while loop.
# Count how many times it takes until the user enters a negative number.
# Stop asking for numbers when a negative is entered.
print(f"\n{hdiv} Question 3 {hdiv}")
print("Negativity")
count = 0
while True: 
    if EMInput(f"Enter any number and I'll see if it's negative\n (Number #{count}): ", "float") < 0:
        break 
    else:
        count += 1 
print(f"It took you {count} numbers until you input a negative number. ")

# 04 - Using an infinite loop, continuously ask the user to keep printing the word “Hi!” to the screen
print(f"\n{hdiv} Question 4 {hdiv}")
print("Hellos")
print("Keep printing the word 'hi'!")
count = 0
while True: 
    if EMInput("").lower() != 'hi': 
        break
    else:
        count += 1
print(f"You printed {count} 'hi's before you stopped!")

# 05 - Ask the user for the capital of France.
# Count how many incorrect guesses it takes until the correct answer is entered.
print(f"\n{hdiv} Question 5 {hdiv}")
print("Questioning")
count = 1
while True: 
    if EMInput(f"What is the capital of the Philippine Islands? \n (Attempt #{count})").lower() == "manila": 
        break
    else:
        count += 1
print(f"It took you {count} attempts to get to the right answer of Manila!")


# 06 - Ask the user for several names.  Count how many names were entered.
# The word “Done” can be used to indicate the user wishes to stop entering.
# Do not count “Done” as one of the names.
# Display a list of all the names after the user is finished.
print(f"\n{hdiv} Question 6 {hdiv}")
print("Naming")
print("Enter a name, or type in 'done' to exit this tool list tool-thingy")
names = []
count = 0
while True: 
    user_input = EMInput("Input: ")
    if user_input.lower() != 'done': 
        names.append(user_input)
        count += 1
    else:
        break
print(f"You listed out {count} names:")
for i in names: 
    print(i)


# 07 - Ask the user for a dollar amount of deposit and rate of interest.
# Determine how many years it would take to become a millionaire.
# Output a chart similar to the one below.
print(f"\n{hdiv} Question 7 {hdiv}")
print("Moooney! ")
principal = round(EMInput("Enter your principal investment in CAD:", "float", "Please enter a number."),2)
interest_rate = EMInput("Enter your rate of interest (in %):", "float", "Please enter a number.")
year = 0
print("Year\t Interest Earned\t Total Investment Value")
while True: 
    interest_income = principal * (interest_rate/100)
    principal = interest_income + principal
    year += 1 
    print(f"{year}\t{interest_income:,.2f}CAD\t{principal:,.2f}CAD")
    if principal >=1000000:
        break



# BONUS (no hints) - Ask the user for a number between 1 and 12 and tell them what month they were born in. 
# Use a while loop to make sure the user enters a number between 1 and 12.
print(f"\n{hdiv} Question 8 {hdiv}")
print("Bonus Question")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
while True: 
    month = EMInput("Enter the number of the month in which you were born!: ", "int", "Please enter a number.")
    if month >= 0 and month <= 12: 
        break
    else:
        print("Please enter a number between 1-12 please.")
print(f"Your month of birth is {months[month-1]}")
