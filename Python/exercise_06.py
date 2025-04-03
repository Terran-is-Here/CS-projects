# Exercise #06
# Name (fill in your name)
# Date (fill in the date)
# This is a program where we practice decision structures using if...Elif...Else statements

# Error Managed Input Function (taken from exercise 05)
# Madatory parameter is input_string; as this is the actual input text. 
# return_type in a string as it's parameter.
# return_type is not mandatory but defaults to input's normal mode; being a string. T
# return_type is BASED AROUND THE FUNCTION THAT TURNS IT INTO THAT DATATYPE; such as string -> str(), integer -> int(), floating-point number -> float(), etc. 
# parameters are used for string formatting; this takes in a dictionary of format key : key value pairs
# error_message is used if the input is invalid with return_type. This is also formatted with the same format key : key value pairs as input_string
hdiv = "="*10
def EMInput(input_string, return_type ="str", parameters={}, error_message = "Error in input. Please try again."): #error-managed number input
    formatted_string = input_string.format(**parameters) #unfolds parameters dictionary as arguments to .format()
    while True:
        try: 
            inputted_value = eval(f"{return_type}(input(formatted_string))")
        except: 
            print(error_message.format(**parameters))
        else:
            return inputted_value

# 01 - Write a program that asks the user for a number and tells them whether it’s odd or even (Hint: modulus %)
print(f"{hdiv} Question 1 {hdiv}")
print("Odd or Even?")
import math
inputted_number = EMInput("Give me a number to calculate if its odd or even: ", "float")
whole_inputted_number = math.trunc(inputted_number) #truncates and removes decimals of inputted_number
if (whole_inputted_number % 2) == 1: #odd condition
    print(f"{inputted_number} is an odd number.")
else:
    print(f"{inputted_number} is an even number.")

# 02 - A store sells lollipops at 50 cents each for small orders or at 30 cents each for orders of 25 lollipops or more.
# Write a program that requests the number of lollipops ordered and displays the total cost.
print(f"{hdiv} Question 2 {hdiv}")
print("Buying Lollipops")
print()
class product:
    Base_price = 0.50 #written in whole dollars
    name = "Lollipops" #object name in plural preferably
    Bulk_purchase_threshold = 25
    Bulk_purchase_price = 0.30 #if bulk purchase threshold is overcome; use this price instead.)
purchase_amount = EMInput("How many {product_name} do you want to purchase?", "int", {"product_name":product.name})

print(f"\n {hdiv}{hdiv}\nTotal cost of your purcahse:")
if purchase_amount >= product.Bulk_purchase_threshold: 
    total_cost = purchase_amount * product.Bulk_purchase_price
    print(f"Buying {purchase_amount}x {product.name} allows you to be appplicable to the discounted bulk purchase cost of {product.Bulk_purchase_price:,.2f}$.")
    print(f"As such, your final cost turns out to be {total_cost:,.2f}$")
else:
    total_cost = purchase_amount * product.Base_price
    print(f"Buying {purchase_amount}x {product.name} is below the threshold needed for the discounted bulk purchase cost of {product.Bulk_purchase_price:,.2f}$.")
    print(f"As such, your final cost turns out to be {total_cost:,.2f}$")

# 03 - Write a program that: Asks for the user’s name, Asks the user to input a number between 1 and 5, 
# and Outputs a personalized insult (that includes the user’s name) depending on which number they picked.
# Keep your insults clean!
# this is mean >:(
print(f"{hdiv} Question 3 {hdiv}")
print("Insulting Inputs.. for some reason.")
print()
username = EMInput("Please give me your name so I can use it to erm... insult you.: ", "str")
insult_id = 0 
insult_list = [
    f"{username}, can you stop procrastinating and get back to work?", 
    f"{username}, the code that you write could be easily rewritten as a recusrive function instead. ",
    f"{username}, you seem like the kind of person to follow a tutorial that makes you enter 'sudo rm -rf \' into your computer. ",
    f"{username}, あなたはばかですか。",
    f"{username}, I'm going to be honest, I ran out of insult ideas."
    ]
insult_amount = len(insult_list) #retuns length of insults
while True: 
    insult_id = EMInput("Now, give me an ID of an insult that you want to recieve (1-{insult_amount}): ", "int",{"insult_amount": insult_amount})
    insult_id = insult_id - 1
    if insult_id >= (insult_amount): 
        print("Could you please pick a number that is actually within the bounds?")
    else:
        break
print(insult_list[insult_id])

# 04 - Write a program that asks the user for their name and which subject they are studying.
print(f"\n{hdiv} Question 4 {hdiv}")
print("Subject_Time")
username = EMInput("Can you now give me your proper name so I can use it to actually help you?: ", "str")
while True: 
    subject = EMInput("What subject are you currently studying right now, {username}?", "str", {"username": username})
    subject_caseedited = subject.lower() #to allow different capitalizations
    match subject_caseedited: 
        case "physics": 
            print(f"{username}, your {subject} class is in B152")
        case "science": 
            print(f"{username}, your {subject} class is in A152")
        case "calculus": 
            print(f"{username}, your {subject} class is in F152")
        case "biology": 
            print(f"{username}, your {subject} class is in Z152")
        case _: 
            print(f"Sorry {username}, I dont recognize that subject. The subjects I recognize are physics, calculus, science and biology. ")
    exit_code = input(f"{username}, do you still want to use this tool? If so, type 1. If not, just type anything else or just press enter: ")
    if exit_code != "1": 
        break

# 05 - Write a program that will ask the user for their name, total hours worked, and regular rate of pay. 
# Overtime pay is double the regular rate of pay.
# If a person works more than 40 hours, they get overtime (otherwise they don’t).  
# Calculate the user's gross pay. (Note-the user might work 2 hours a week, the user might work 42 hours a week).
print(f"\n{hdiv} Question 5 {hdiv}")
print("Income Calculator")

overtime_hour_threshold = 40
overtime_pay_modifier = 2 
overtime_pay = 0 

user = EMInput("Who am I calculating the income of?: ", "str")
pay_rate = EMInput("What is {user}'s normal hourly pay rate?: ", "float", {"user": user})
hours_worked = EMInput("How many hours did {user} work this week?: ", "float", {"user": user})
overtime_hours = hours_worked - overtime_hour_threshold


print(hdiv*3)
print("Normal Hours Worked income: ")
if hours_worked >= 40: 
    normal_income = pay_rate * 40
    print(f"Hours worked: 40")
    print(f"Regular Rate: {pay_rate}$/hr")
    print(f"Gross Income: {normal_income:,.2f}$")
else: 
    normal_income = pay_rate * hours_worked
    print(f"Hours worked: {hours_worked}.")
    print(f"Regular Rate: {pay_rate:,.2f}$/hr")
    print(f"Gross Income: {normal_income:,.2f}$/hr")

    
if overtime_hours > 0: 
    overtime_pay = overtime_hours * pay_rate * overtime_pay_modifier
    print(hdiv * 3)
    print(f"Overtime Pay of {user}: ")
    print(f"Overtime Hours: {overtime_hours} hrs")
    print(f"Overtime Rate: {pay_rate * overtime_pay_modifier:,.2f}$/hr")
    print(f"Gross Income: {overtime_pay:,.2f}$")
print(hdiv*3)
print(f"Final Gross Income of {user}: {normal_income + overtime_pay:,.2f}$")

# 06 - Create your own quiz with five or more questions that are True and False.
# Keep track of the user's score, and at the end show them what percentage of the questions they got right.

print(f"\n{hdiv} Question 6 {hdiv}")
print("Math Quiz")
import random
print("\n Please enter only True or False for these questions (not case sensitive)")
questions = [
    "A derivative by definition can only be done on a fully continuous function (atleast within it's domain).\nDoes the same statement hold true for the converse; that all continuous functions are differentiable?",
    "Given the sinusoidal function f(x) = sin(x); Is it true that the following integral would give a non-zero answer?: \nLow Bound: -x, \nUpper Bound +x",
    "Is the following equality correct? \n(3x+2i)(2x-3i) =  6x^2 - 5ix + 6",
    "Given the function f(x) = 1/x, is the following statement true? \n The limit of f(x) as it approaches 0 exists.",
    "Given the function f(x) = 1/x, is the following statement true? \n There exists two different one-sided limits to f(x) as it approaches 0."
]
question_amount = len(questions)
answers = [
    "False",
    "False",
    "True",
    "False",
    "True",
]
score = 0
for i in range(1,len(questions)+1): #index-shifted by one to prevent off-by-one errors
    question_chosen = random.randint(0,len(questions)-1) #randomly picks question in the range of questions - 1 (since 0-indexing)
    print(f"\nQuestion {i}: \n{questions[question_chosen]}")
    #print(answers[question_chosen])
    response = EMInput("Input Answer Here: ", "str")
    if response.upper() == answers[question_chosen].upper(): #capitalization ignoring; allows for multi-capitalized inputs
        score += 1 
    questions.pop(question_chosen) #removes question at question_chosen index from the questions list
    answers.pop(question_chosen) #does the same as above but for answers instead.
print(f"Score: {score} / {question_amount} ({(score/question_amount)*100:,.2f}%)")