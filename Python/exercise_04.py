# Exercise #04
# Name: Pablo Luis Cauton
# Date (fill in the date)
# This is a program where we practice getting and using user input, storing them in variables, and outputting the result properly formatted.

# 01 - Input marks for 4 classes and calculate the average grade. Print the marks formatted with a percent sign. 
# Print the average formatted with a percent sign and TWO decimal places

print("Q1: Mark Averager") 
courses = [] # define an empty table of course values
total_marks = 0 # defines total marks as an empty memory buffer value 
for i in range(0,4):
    current_courses = (input("Input course code:"),float(input("Input your mark for said course: "))) #stores current marks as a tuple
    total_marks = total_marks + current_courses[1] # total marks = adding the second value of a tuple (the float())
    courses.append(current_courses) 
print("Marks:")
for i in range(0,4): #iterates and displays tuple contents at index i
    print(f"{courses[i][0]}: {courses[i][1]}%")
# calculates the average, multiplies it by 100, then uses round() to remove decimals then divides by 100 to get 2 DP precision.
print(f"Average Mark: {round((total_marks/4)*100)/100}%")
print()

# 02 - Determine what the dollar amount of sales tax is between two prices and what percent of sales tax was imposed on the item. 
print("Q2: Sales Tax Calculator") 
original_price = float(input("Enter the original price of the item: "))
final_price = float(input("Enter the final price of the item: "))
tax_amt = final_price-original_price
tax_rate = (tax_amt/original_price)*100

print(f"Original Price: {original_price}$")
print(f"Final Price: {final_price}$")
print(f"Tax Rate:  {round(tax_rate,2)}%") 
print(f"Taxed Amount: {tax_amt:,}$")
print()

# 03 - A factory produces fidget spinners. They sell them in packages of 12. How many packages are produced in a day? 
# Indicate how many full boxes are required and how many spinners would be left over. HINT(use integer division // and modulus division % )
print("Q3: Fidget Spinner Question")
spinners_produced = int(input("How many fidget spinners are produced?: "))
Fidget_spinner_box_cap = 12 #change in case of different package sizes 

remaining_fidget_spinners = spinners_produced%Fidget_spinner_box_cap ##remainder
containers_used = spinners_produced//Fidget_spinner_box_cap ##modulo for clean division 

print("------")
print(f"Assuming containers can contain {Fidget_spinner_box_cap} spinners:")
print(f"Full Boxes Required: {containers_used:,.3f} Boxes")
print(f"Unpackaged Spinners: {remaining_fidget_spinners} Spinners")
print()


# 04 - Calculate the total pay, tax, and take-home pay of an employee who is deducted 25% in taxes off their overall pay.
print("Q4: Payroll Calculator")
hours_worked = float(input("How many hours did you work this week?: "))
hourly_income = float(input("How much hourly income do you make?: "))
gross_income = hours_worked * hourly_income
taxed_income = gross_income*0.25
final_income = gross_income*0.75
print(f"{"-"*20}")
print(f"Assuming that you worked {hours_worked} hours with a hourly rate of {hourly_income}$:") #displays income segments
print(f"Gross income: {gross_income:.2f}$")
print(f"Taxed income: {taxed_income:.2f}$")
print(f"Take-home pay / final income: {final_income:.2f}$")
print()
# 05 - Ask the user for the name of an item, its price, and the quantity ordered. 
# Calculate and display the total price before tax, and after tax. (HST = 13%). 
# Then ask the user for the amount they will be paying with. 
# Display the amount of change they are to receive. 

print("Q5: Buying Calculator")
item = input("What item are you trying to buy? ")
item_cost = float(input(f"How much does one {item} cost?: "))
item_amt = int(input(f"How many {item}s are you buying?: "))
tax_rate = 0.13 # change for different tax amounts 
final_cost = round(item_amt*item_cost*(1+tax_rate),2)
print(f"{"-"*20}")
print(f"Initial price before tax: {item_cost*item_amt}$")
print(f"Taxed amount: {round(item_cost*item_amt*tax_rate,2)}$") #rounded to 2DP for the taxed amount.
print(f"Final price after tax: {final_cost}$\n")
payment_amt = float(input(f"Please enter payment amount for buying {item_amt} {item}s ({final_cost}$): "))
# simple if-else statement for insufficient funds. 
if payment_amt < final_cost: 
    print("Insufficient funds.")
else:
    print(f"Remaining change: {(payment_amt-final_cost):.2f}$")
    print(f"Thank you for buying {item}s with us.")


