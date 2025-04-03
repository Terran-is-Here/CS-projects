# Assignment #01
# Name Pablo Luis Cauton
# Date 2025-03-17
# Cumulative Task

# 01 - Write a program to form the name of a knight by asking the user for the knight’s name and a personality characteristic.
# The final name should be printed as “Sir <name> the <characteristic>.”
# For example, if the user enters # “Robin” and “Brave,” you would print “Sir Robin the Brave.”
print(f"{'='*5} Question 1 {'='*5}")
print("Knighthood")
knight_name = input("What is thou name, dear knight?")
knight_characteristic = input("What character of heart does thou have?")
knight_origin = input("Where art thou from?: ")
print(f"Welcome Sir {knight_name} the {knight_characteristic}, Knight of {knight_origin}. Welcome to my assignment project.")
print()

# 02 - Write a program that asks the user for 3 numbers then outputs the average of those 3 numbers rounded to one decimal place.
print(f"{'='*5} Question 2 {'='*5}")
print("Numerical Averages")
numbers_to_calculate = 3 #setting, can be changed with different numbers
print(f"Give me {numbers_to_calculate} numbers to calculate the average of!")
values = []
sum = 0
for i in range(0,numbers_to_calculate): #performs code below numbers_to_calculate times. 
    new_value = float(input(f"Number {i+1} / {numbers_to_calculate}: ")) #stores value in a temporary variable
    values.append(new_value) #appends new_value to the end of the list of values
    sum = sum + new_value #adds new value to the sum of current values for the average
print(f"Your number selection: {values}")
print(f"Their average: {(sum/numbers_to_calculate):.2f}")
print()
# 03 - Ask a user for their name and age and tell them how many years it will be until they turn 21
print(f"{'='*5} Question 3 {'='*5}")
print("Age Calculator")
print()
goal_age = 21 #setting, can be changed.
name = input("What is your name? ")
current_age = int(input("What is your current age in years?"))
print(f"It will take you ({name}) {goal_age-current_age} years to turn {goal_age}.")
print()
# 04 - Ask the user to input the number of miles. You'll convert miles to kilometers (kilometers = miles * 1.60934)
# round your answer to 1 decimal place
print(f"{'='*5} Question 4 {'='*5}")
print("Miles to Kilometers Calculator")
print()
miles = float(input("This is a Miles to Kilometers converter. Input number of miles: "))
print(f"{miles}mi => {round((miles*1.60934),1)}km.")
print()
# 05 - Write a program that calculates the tax of an item.  Assuming a tax rate of 13%.
print(f"{'='*5} Question 5 {'='*5}")
print("Tax Calculator")
print()
tax_percentage = 0.13 #straight percentage, e.g =0.13 -> 13% tax. 
item_name = input("Give me the name of the item you want to calculate the tax for: ")
item_amt = int(input("How many items are you going to buy?: "))
item_cost = float(input(f"Give me the cost of a single one of your item ({item_name})?: "))

taxed_cost = item_cost * item_amt * tax_percentage
final_cost = item_cost * item_amt * (1 + tax_percentage)
#f-strings below formatted to 2DP precision. 
print(f"{"="*20}")
print(f"{item_amt}x {item_name} subtotal: ${(item_cost*item_amt):.2f}")
print(f"Tax: ${taxed_cost:.2f} (assuming a tax rate of {tax_percentage}%)")
print(f"Final Total: ${final_cost:.2f}")