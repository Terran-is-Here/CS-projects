# Exercise #05
# Pablo Luis Cauton
# 2025-03-19
# This is a program where we practice decision structures using if...else statements
hdiv = "="*7 # horizontal divider segment

# Error Managed Input Function
# Madatory parameter is input_string; as this is the actual input text. 
# return_type in a string as it's parameter.
# return_type is not mandatory but defaults to input's normal mode; being a string. T
# return_type is BASED AROUND THE FUNCTION THAT TURNS IT INTO THAT DATATYPE; such as string -> str(), integer -> int(), floating-point number -> float(), etc. 
# parameters are used for string formatting; this takes in a dictionary of format key : key value pairs
# error_message is used if the input is invalid with return_type. This is also formatted with the same format key : key value pairs as input_string

def EMInput(input_string, return_type ="str", parameters={}, error_message = "Error in input. Please try again."): #error-managed number input
    formatted_string = input_string.format(**parameters) #unfolds parameters dictionary as arguments to .format()
    while True:
        try: 
            inputted_value = eval(f"{return_type}(input(formatted_string))")
        except: 
            print(error_message.format(**parameters))
        else:
            return inputted_value

# 01  - Write a program that asks the user to input their name.
# If they enter 'Steve' then the program outputs 'Hello Steve', else: "This message is for Steve only"
# Be careful when testing, Steve and steve are NOT the same thing.

print(f"{hdiv} Question 1 {hdiv}")
print("If-Then messages")
passname = "Pablo" #can include spaces
entered_name = input(f"The following message is meant only for a certain individual. Who are you? ")
if entered_name.lower() == passname.lower(): #ensures that the string can be compared based on character structure, not on capitalization.
    print(f"Hello {entered_name}, this is the message that I wanted to say: \n Can you please remember for once not to procrastinate? ")
else:
    print(f"Sorry {entered_name}, this message was only meant for {passname}.")



# 02  - Write a program that asks the user to input their age.
# If they enter 16 or older, the program outputs "You are old enough to drive"
# else: "You are NOT old enough to drive"
print()
print(f"{hdiv} Question 2 {hdiv}")
print("Driving Legality")
driving_legal_age = 16 #legal age in years
user_age = EMInput("How many years old are you; {entered_name}?: ", "float",{"entered_name": entered_name})
if user_age >= driving_legal_age: 
    print(f"Congratulations {entered_name}, you can drive legally!")
else:
    print(f"Sorry {entered_name}, you cannot (legally) drive yet.")



# 03 - Write a program that asks the user to input a number between 1 and 10.
# If they enter '8' then the program outputs the number with "x is my favorite number"
# else: the number with "x is not my favorite number"
print()
print(f"{hdiv} Question 3 {hdiv}")
print("Favourite Numbers")

### === Random Number Generation variant === ###
import random
bounds = (0,10) #both bounds are inclusive
favourite_number = random.randint(bounds[0], bounds[1])
print(f"Favourite Number: {favourite_number}") #debug tool
# constant random number variant
# favourite_number = 0 #must be a float

while True: 
    entered_number = int(input(f"Give me a number, {entered_name} between {bounds[0]} and {bounds[1]} inclusive. I'll tell you if it is my favourite: "))
    if entered_number > bounds[1]: 
        print(f"I told you to enter a number between {bounds[0]} and {bounds[1]} >:(")
    elif entered_number == favourite_number: 
        print(f"Congratuations, you guessed my favourite number!")
        break
    else: 
        print(f"Not quite right, {entered_number} is not my favourite number.")
    

# 04 - Write a program that will ask the user for a number.
# If the number entered is negative, display a message "X is a negative number”
# else: "X is a positive number".
print()
print(f"{hdiv} Question 4 {hdiv}")
print("Number Signs")

while True: # basic attempt at input error management
    try: 
        entered_number = float(input(f"{entered_name}, please give me a number to find the sign for: "))
    except: #if the above expression returns an error (such as float() taking in a string, runs code below.
        print(f"Please enter a proper number this time {entered_name}.")
    else: #if code above runs without problems, breaks out of the while loop
        break

if entered_number > 0: 
    print(f"{entered_name}, {entered_number} is positive.")

elif entered_number < 0: 
    print(f"{entered_name}, {entered_number} is negative.")

else: 
    print(f"{entered_name}, {entered_number} is... 0")

# 05 - Ask the user to enter a password.  If the credentials are acceptable, display the message “ACCESS GRANTED”.
# Otherwise, display the message “ACCESS DENIED”.
print()
print(f"{hdiv} Question 5 {hdiv}")
print("password time")

password= "testing1234"
print(f"For testing purposes; the password is {password}") #debug tool
entered_password = input(f"A password is required, {entered_name}, to access this secret message:")
if entered_password == password: 
    print(f"Access Granted, {entered_name}. \nThe message is, that you have just lost The Game :3.")
else:
    print(f"ACCESS DENIED \nYou honestly didnt want to read what was in the other edge case :3")


# 06 - Write a program to find the larger of two numbers inputted by the user. Tell the user which one is greater.
print()
print(f"{hdiv} Question 6 {hdiv}")
print("Larger Numbers")

print(f"\n {entered_name}, please enter two numbers for me to compare which one is greater.")
number1 = EMInput("Your first number: ", "float")
number2 = EMInput("Your second number: ", "float")
if number1 > number2: 
    print(f"{number1} was greater than {number2}")
elif number1<number2:
    print(f"{number2} is larger than {number1}")
elif number1 == number2:
    print(f"{number1} is... {number2}...")

# 07 - Write a program that will determine the net profit or loss of a company.
# The formula for net profit is: Net Profit = Revenue - Expenses
# If there are more Expenses than there is Revenue then the end result is a negative number.
print()
print(f"{hdiv} Question 7 {hdiv}")
print("Profit's Calculation")
print(f"\n {entered_name} Corp. Profit Calculator.")
revenue = EMInput("Enter revenue earned during this financial quarter: ", "float")
expenses = EMInput("Enter operating expenses during this financial quarter: ", "float")
net_profit = revenue - expenses
return_on_operating_expenses = (net_profit / expenses)*100 #percentage
if net_profit < 0: 
    print(f"We have lost {abs(net_profit):,.2f}$. We are SO cooked.")
    print(f"Our return on Operating Expenses was {return_on_operating_expenses:,.2f}%. damn.")
elif net_profit > 0:
    print(f"We were able to make a profit of {net_profit:,.2f}$. Investors are going to love this.")
    print(f"Our return on operating expenses for this quarter was {return_on_operating_expenses:,.2f}%.")
elif net_profit == 0: 
    print(f"We just barely broke even on our operating expenses. ")

# 08 - Write a program that will calculate a salesperson's salary including commission.
# Ask the user for their name and weekly sales.  If they made over $200 in sales they earn an extra 5% of sales.
# Everyone earns $300 per week as their base pay. Calculate the person's final pay.
print()
print(f"{hdiv} Question 8 {hdiv}")
print("Salary Calculation")
print(f"\n\n {entered_name} Corporation Employee Pay-inator calculator (tm pending)")
salesperson_name = EMInput("What is the name of the salesperson you want to calculate the income of?: ", "str")
salesperson_sales = EMInput("How much money did they make in their weekly sales?: ", "float") 
base_pay = 300
if salesperson_sales > 200: 
    salesperson_comission = salesperson_sales * 0.05
else:
    salesperson_comission = 0
final_pay = base_pay + salesperson_comission
print(f"{salesperson_name}'s final income for this week (with {salesperson_sales:,.2f}$ worth of weekly sales) is:\n {final_pay:,.2f}$")
if salesperson_comission > 0: 
    print(f"{salesperson_name} had a commission bonus of {salesperson_comission:,.2f}$ uwu :3")
else: 
    print(f"{salesperson_name} was not eligable to gain a commission bonus.")
