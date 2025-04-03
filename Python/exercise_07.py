# Exercise #07
# Name Pablo Luis Cauton    
# Date 2025-03-25
# This is a program where we practice using if...Elif...Else statements and Nested if statements
hdiv = "="*10
#EMInput() documentation present in exercise 05-06. This version is mildly updated to now differentiate between KeyboardInterrupt and ValueError exceptions.
import sys
def EMInput(input_string, return_type ="str", parameters={}, error_message = "Error in input. Please try again."): #error-managed number input
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
    
# 01 - Write a program that asks for the user’s age. If the user is under 13, output, “You are a child”.
# For 13 to 19, output, “You are a teenager”. From 20 to 65, “You are an adult”. Over 65, “You are a senior”.
# Print out "Not a valid age" for the else statement.
print("\n")
print(f"{hdiv} Question 1 {hdiv}")
print(f"Age Thingy (look, I dont know either.)")
username = EMInput("What is your name (for the future reference of this program): ", "str")
user_age = EMInput("How old are you, {user}?: ", "int", {"user":username}, "Please enter a proper integer input.")

if user_age < 0:
    print(f"Invalid age. How can one be negative years old? ") 
elif user_age <= 13: 
    print(f"Sorry {username}, thoust is a child.")
elif user_age <=19: 
    print(f"Woah, {username}, thoust is a teenager")
elif user_age <= 65: 
    print(f"Woah, {username}, you are an adult.")
else: #edge case handled by user_age or EMInput's try setting.
    print(f"Sorry, {username}, you are a senior.")

# 02 - Write a program to help parents decide what car seat they should use based on the information below.
# None needed if weight is greater than 80lb or height is above 145 or age is greater than 8.
# Forward Facing Car seat if weight is greater than 20lb up to 40lb
# Rear face Car seat from zero up to at least 20lb.
# Booster seat would be what's not covered (the else statement).
print("\n")
print(f"{hdiv} Question 2 {hdiv}")
print(f"Car Seat Picker")

class child: 
    name = EMInput("What is their name?: ", "str")
    age = EMInput("How old is the passenger you want to have the car seat for?", "float")
    height = EMInput("How tall are they (in centimeters): ", "float")
    weight = EMInput("What is their weight (in pounds)?: ", "float")
if child.height > 145 or child.age > 8 or child.weight > 80: 
    print(f"{child.name} does not require a car seat to ride safely in a car.")
elif child.weight > 20 and child.weight <= 40: 
    print(f"{child.name} would be safest using the Forward Facing Car seat.")
elif child.weight >= 0 and child.weight <= 20:
    print(f"{child.name} would be safect using the Rear Facing car seat.")
else:
    print(f"The booster seat is the safest choice for {child.name}.")


# 03 - You and your date are trying to get a table at a restaurant. The stylishness of your clothes is rated in the range from 0...10.
# Scenario #1 - If both of your styles are perfect 10s, you get a table in the back with the chef
# Scenario #2 - If either one of you has a style of 2 or less, you will definitely NOT get a table
# Scenario #3 - If either one of you is very stylish (8 or above), then you will get a table
# Scenario #4 - Otherwise you might get a table.
print("\n")
print(f"{hdiv} Question 3 {hdiv}")
print(f"Date Table Calculator")

date_name = input(f"What is the name of your date, {username}?: ")

while True: 
    user_style_rating = EMInput("How stylish are you {username}, on a scale of 0-10 (inclusive): ", "float", {"username":username}, "Please enter a number.")
    date_style_rating = EMInput("How stylish is your date, {date_name}, on a scale of 0-10 (inclusive): ", "float", {"date_name":date_name}, "Please enter a number.")
    if user_style_rating < 0 or date_style_rating < 0: #checks if value is under 0, which dosent really make sence for a scale. 10+ is alright as its like; exaggerating their value. 
        print(f"Please enter numbers atleast bigger than 0 please.")
    else:
        break
if user_style_rating >= 10 and date_style_rating >= 10: 
    print(f"{username}, you and {date_name} will guaranteed to be able to get a table in the back with the chef!")
elif user_style_rating <= 2 or date_style_rating <= 2: 
    print(f"Sorry {username}, you and {date_name} will NOT get a table.")
elif user_style_rating >=8 or date_style_rating >= 8: 
    print(f"{username}, you and {date_name} will get a table.")
else:
    print(f"{username}, we can only say that for your date with {date_name}, we can only say that you have the possibility of getting a table.")

# 04 - I only like to go for a run if the temperature is between 20 and 30 degrees Celsius (inclusive). 
# Unless it is summer, then the upper limit is 35 instead of 30. 
# Ask the user for the current temperature and whether or not it is summer, and output whether or not I should go for a run.
print("\n")
print(f"{hdiv} Question 4 {hdiv}")
print(f"Running Weather Checker")

class weather: 
    temperature = EMInput("What is the temperature outside right now (in celsius): ", "float")
    season = EMInput("What is the current season outside right now?", "str")

if weather.season.lower() == "summer": 
    if weather.temperature >= 20 and weather.temperature <=35:
        print(f"Its summer right now, so its a good time to go on a run {username}.") 
    else:
        print("Now's not a good time to go on a run.")
elif weather.temperature >= 20 and weather.temperature <=30: 
    print(f"Its a good time to go on a run right now, {username}.")
else:
    print("Now's not a good time to go on a run.")

# 05 - You are driving a little too fast, and a police officer stops you. 
# Ask the user for their speed and whether or not it is their birthday, 
# and output whether or not they get no ticket, a $50 ticket, or a $200 ticket.
# Scenario #1 - If you drive 80 km/h or less you won’t get a ticket.
# Scenario #2 - if you drive faster than 80 km/h but less than 100 km/h you will get a $50 ticket.
# Scenario #3 - If you drive faster than 100 km/h you will get a $200 ticket.
# Scenario #4 - Unless of course it is your birthday -- on that day, your speed can be 5 km/h higher in all cases. 
# You should also wish them a Happy Birthday
print("\n")
print(f"{hdiv} Question 5 {hdiv}")
print(f"Traffic Ticket thingy")

speed = EMInput("What speed were you travelling (km/hr)?: ", "float") 
Birthday = EMInput("{username}, is it your birthday today (y/n)?: ", "str", {"username":username}) 
class speed_limits:
    lower = 80 #lower speed limit for 50$
    higher = 100 #higher speed limit for 200$
    birthday_modifier = 5 #birthday speed modifier
if Birthday.lower() == "y": 
    print(f"Happy birthday {username}!")
    if speed <= (speed_limits.lower + speed_limits.birthday_modifier): 
        print(f"You dont have to worry about getting a ticket {username}!")
    elif speed > (speed_limits.lower + speed_limits.birthday_modifier) and speed <= (speed_limits.higher + speed_limits.birthday_modifier): 
        print(f"Sorry {username}, you will get a 50$ ticket :(")
    elif speed > (speed_limits.higher + speed_limits.birthday_modifier):
        print(f"Sorry {username}, you will have to pay a 200$ ticket.")
else:
    if speed <= (speed_limits.lower): 
        print(f"You dont have to worry about getting a ticket {username}!")
    elif speed > (speed_limits.lower) and speed <= (speed_limits.higher): 
        print(f"Sorry {username}, you will get a 50$ ticket :(")
    elif speed > (speed_limits.higher):
        print(f"Sorry {username}, you will have to pay a 200$ ticket.")


# 06 - You keep sleeping in and getting to school late, so you decide to make an alarm clock program.
# The alarm clock accepts as input the day of the week and whether or not the user is on vacation.
# On weekdays, the alarm outputs “7:00” as the time to wake up, and “10:00” is outputted on the weekend. 
# However, if the user is on vacation, the alarm outputs “10:00” on weekdays, and “off” on weekends.
print("\n")
print(f"{hdiv} Question 6 {hdiv}")
print(f"Alarmingly Late")

#days below must be written in all lower case (as the .lowers() below necessitates it.)
class Days: 
    weekends = ["saturday", "sunday"]
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
class Alarm_Clock: 
    weekend_alarm = "10:00"
    normal_alarm = "7:00"
class current_time: 
    day = "" #null value to initialize variable in class
    vacation_status = "" #null value to initialize variable in the class for ease later

#both loops below ensure proper data is entered.
while True: 
    current_time.vacation_status = EMInput("Are you on vacation right now (Yes or No)?: ", "str").upper() #expects a string to be returned
    if current_time.vacation_status == "YES" or current_time.vacation_status == "NO": 
        break
    else:
        print("Please enter a valid yes or no value.\n")

while True: 
    current_time.day = EMInput("What day is it right now?: ", "str").lower() #expects a string to be returned
    if (current_time.day in Days.weekdays) == True or (current_time.day in Days.weekends) == True:
        break
    else:
        print("Please enter a valid date\n")


if current_time.vacation_status == "YES": 
    if (current_time.day in Days.weekends) == True: #checks if date is in the list of weekend days. 
        print("Your alarm is off.")
    else: #if above condition is false, date must be a weekday.
        print(f"You have to wake up at {Alarm_Clock.weekend_alarm}")
else: 
    if (current_time.day in Days.weekends) == True: #checks if date is in the list of weekend days. 
        print(f"You have to wake up at {Alarm_Clock.weekend_alarm}")
    else: #if above condition is false, date must be a weekday.
        print(f"You have to wake up at {Alarm_Clock.normal_alarm}")



