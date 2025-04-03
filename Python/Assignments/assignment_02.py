# Assignment #02
# Name Pablo Luis Cauton
# Date 2025-03-31
# Cumulative Task

#Error handling input statement; taken from exercise_07.py
#hdiv statements also taken from previous assignments for formatting
#i am aware that the function below can be massively shortened to just a try statement; I didnt know that you can directly pass F-strings as parameters in functions.
#this change will be hopefully put into effect in exercise_08
import sys
hdiv = "="*10
def EMInput(input_string, return_type ="str", parameters={}, error_message = "Error in input. Please try again."): 
    formatted_string = input_string.format(**parameters) #unfolds parameters dictionary as arguments to .format()
    while True:
        try: 
            inputted_value = eval(f"{return_type}(input(formatted_string))")
        except KeyboardInterrupt: 
            print("\nExiting program due to KeyboardInterrupt.")
            sys.exit() #re-implements forced exit on Ctrl+C KeyboardInterrupt errors.
        except ValueError: 
            print(error_message.format(**parameters)) # will handle type-matching errors, like inputting a string to a int()
        else:
            return inputted_value


# 01 - Write a program that asks the user to input their age and tells them if they're old enough to ride a roller coaster. 
# The minimum age to ride the roller coaster is 13.
print("\n")
print(f"{hdiv} Question 1 {hdiv}")
print("Roller Coaster viability go brrr")

Username = EMInput("What is your name?: ")
age = EMInput("How old are you?\n (Input amount of years old): ", "float")
if age >= 13: 
    print(f"{Username}, you are old enough to ride this roller coaster! ")
else:
    print(f"{Username}, you are not old enough to ride this roller coaster. ")

# 02 - You are going to write a tip calculating program that does the following:
# Ask the user to enter the subtotal of a restaurant bill
# Ask the user if they wish to enter a tip, and if they do, let them enter the tip by a percentage of the subtotal.
# Display the receipt:  Subtotal, Taxed Owed (13%), Tip, Grand Total
print("\n")
print(f"{hdiv} Question 2 {hdiv}")
print("Tipping off the work")
print("\n Pablo's Store (Checkout)")

Subtotal = EMInput("What is the subtotal of the items that your purchased?: ", "float", {}, "Please enter a valid number")

tax = 0.13 # tax rate, adjustable
taxes_owed = Subtotal * tax

tip_amount = 0 # defines as 0 in case of bottom if statement not succeeding 

tip_status = EMInput("Do you want to give us a tip (Yes or No)?: ", "str").lower() #forces case of status to lowercase.
while True: #loops through until transaction is finished / calculator is closed
    while True: #loops through until a tip is finished
        if tip_status == "yes": 
            tip_percentage = EMInput("\nPlease enter a percentage of your subtotal ({subtotal}) that you would like to tip to us. \nFor inputting, please enter the tip percentage as a decimal (e.g 13% tip is 0.13 input)\nYour tip: ", "float", {"subtotal":Subtotal},"Please enter a valid number.")
            tip_amount = Subtotal * tip_percentage #calculates tip amount

            #confirmation if the user really wants to pay their tip amount
            tip_confirmed = EMInput(f"\nYou will give us a tip of {tip_amount:,.2f}$. \nAre you sure that you want to perform this action (Yes or No)?: ").lower()
            if tip_confirmed == "yes": #if they confirm this tip amount, breaks out of the first nested loop
                break
            else: #else; asks if they still want to do a tip; this floows back into the if condition wrapping this code and the else statement breaks us out.
                tip_status = EMInput("Do you still want to give us a tip (Yes or No)?: ", "str").lower()
        else: #only procs if they dont agree to a tip; or the above line is a value other than "yes", in which case breaks out of the tipping loop
            break
    print(f"{hdiv*3} Transaction Summary {hdiv*3}") #displaying transaction details
    print(f"Subtotal: {Subtotal:,.2f}$")
    print(f"Taxed Amount: {taxes_owed:,.2f}$")
    if tip_amount > 0: 
        print(f"Tip amount ({tip_percentage*100}% tip): {tip_amount:,.2f}$")
    print(hdiv*3)
    print(f"Total: {(Subtotal + taxes_owed + tip_amount):.2f}$")

# transaction loop break logic
    if EMInput("Are you sure that you want to finish this transaction? \n(Yes or No): ").lower() == "yes": 
        print("Thank you for your business"); break #if user is happy, escapes outermost loop.
    else:
        transaction_status =  EMInput("Do you want to perform another transaction? \n(Enter No to exit; entering anything else will restart this entire calculator.): ").lower() #in the case this isnt yes; does not proc the break condition below and restarts the entire loop.
        if transaction_status == "no": 
            print("Oh, shame. Thanks for using this tool though.");break #else, break out of the loop 

# 03 - Write a program that outputs the fine given to a driver for going over the speed limit.
# 1 to 20 km/h over the limit = $100 Fine
# 21 to 30 km/h over the limit = $250 Fine
# 31 or more km/h over the limit = $500 Fine
print("\n")
print(f"{hdiv} Question 3 {hdiv}")
print("Speed Ticket Calculator")


speed_limit = 100 
speed = EMInput("How fast were you going\n (Input in km/h): ", "float")
if speed > speed_limit: #simple if-elif logic
    print("Thank you for the honesty.")
    speed_over_speed_limit = speed - speed_limit
    if speed_over_speed_limit > 0 and speed_over_speed_limit <= 20: 
        print(f"Sorry {Username}, you have to pay a 100$ fine.")
    elif speed_over_speed_limit > 20 and speed_over_speed_limit <= 30: 
        print(f"Sorry {Username}, you have to pay a 250$ fine.")
    elif speed_over_speed_limit > 30: 
        print(f"Sorry {Username}, you have to pay a 500$ fine.")
    else: #deals with impossible edge case, just in case.
        print(f"Oh, so you went under the speed limit, or you caused an integer overflow error. Either way, not a good use of our time.")
else: 
    print("Oh, ok. Have a nice day I guess.")