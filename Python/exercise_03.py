# Exercise #03
# Name Pablo Luis Cauton
# Date 2025-02-27
# This is a program where we practice getting and using user input and storing them in variables.


# 01 - Ask the user for their name. Store your name in a variable then display the greetings message.
user_name = input("What is your name?:")
myname="Pablo";
print(f"Welcome {user_name} to this little input() exercise program made by {myname}!")

# 02 - Ask the user for their favorite color. Store the color in a variable then display the message.
favourite_color = input("What is your favourite color?: ")
print(f"Alright, thank you. Ill make sure to make my next website with a proper color selections including {favourite_color}")

# 03 - Ask the user for the length and width of a rectangle. Display the area of the rectangle.
print("\nRectangle (Q3)\n please state the following measurements for a rectangle.")
length = float(input("State the length of such rectangle:"))
width = float(input("State the width of such rectangle:"))
print(f"The area of the rectangle is {length} * {width} = {length*width}")

# 04 - Ask the user for the length and width of a rectangle. Display the perimeter of the rectangle.
print("\nRectangle (Q4)\n please state the following measurements for a different rectangle.")
length = float(input("State the length of such rectangle:"))
width = float(input("State the width of such rectangle:"))
print(f"The area of the rectangle is 2* {length} + 2* {width} = {2*(length+width)}")

# 05 - Ask the user for a Celsius temperature. Display the equivalent temperature in Fahrenheit.
print("\n Q5: Celsius to Farenheit temperature conversion.")
temperature_celsius = float(input("Give me a Celscius temperature, and I shall convert it into Farenheit!: "))
temperature_farenheit = (9/5) * temperature_celsius + 32
print(f"{temperature_celsius}C = {temperature_farenheit}F :)")

# 06 - Ask the user for a Fahrenheit temperature. Display the equivalent temperature in Celsius.
print("\n Q6: Farenheit to Celsius temperature conversion.")
temperature_farenheit = float(input("Give me a Farenheit temperature, and I shall convert it into Celscius!: "))
temperature_celsius = (5/9) * (temperature_farenheit - 32)
print(f"{temperature_farenheit}F = {temperature_celsius}C :)")


# 07 - Ask the user for the lengths of four long jumps. Display the sum and average of these four jumps.
print("\nQ7: Long Jump questions.\nGive me the lengths of 4 long jumps (in meters, WITHOUT THE UNIT), and I shall calculate the average! ")
long_jump_values = []
long_jump_total = 0
for i in range(0,4):
    long_jump_values.append(float(input(f"Long jump #{i+1} value: ")))
    long_jump_total = long_jump_total + long_jump_values[i]
long_jump_average = long_jump_total / 4
print(f"Long jump values: {long_jump_values}")
print(f"Long jump total distances: {long_jump_total}")
print(f"Average long jump distance: {long_jump_average}m")

# 08 - Ask the user to enter two numbers. Output the results of addition, subtraction, multiplication, division, and modulus. Display the results.
print("\nQ8: Numerical Operations.\nGive me 2 numbers, and I shall show you what some operations on them look like! \n NON-ZERO NUMBERS PLEASE.")
operations_list = ['+','-','/','*','%']
values = [float(input("Number #1: ")),float(input("Number #2: "))]

for operation in operations_list: 
    print(f"{values[0]} {operation} {values[1]} = {eval(str(values[0]) + operation + str(values[1]))}")

for operation in operations_list: 
    print(f"{values[1]} {operation} {values[0]} = {eval(str(values[1]) + operation + str(values[0]))}")

# 09 - Ask the user to enter a two-digit whole number. Display the two digits separately to the user. (Hint: use the mod operator).
print("\nQ9: 2 Digits.\nGive me a number and I shall split it up into 2!")
tbs_number = str(input("gimme the number >:)"))
for i in tbs_number:
    print(i)
    
# 10 - Ask the user to enter an amount of change of less than one dollar.
# Calculate and display the minimum number of quarters, dimes, nickels, and pennies necessary to make the change. (Hint: mod again!)
print("\nQ10: Coin Management\n")
change=int(input("Give me some change (money below 1$) as a whole number (e.g 0.57 -> input as 57):"))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

quarters = change//25
print(f"# of quarters needed: {quarters}")
change = change%25

dimes = change//10
print(f"# of dimes needed: {dimes}")
change = change%10

nickels = change//5
print(f"# of nickels needed: {nickels}")
change = change%5

pennies = change
print(f"# of pennies needed: {pennies}")
# ###Quarter: 25 cents
# Dime: 10 cents
# Nickel: 5 cents
# Penny: 1 cent