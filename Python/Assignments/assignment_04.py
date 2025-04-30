# Assignment #04
# Name Pablo Luis Cauton
# Date 2025-04-30
# Cumulative Task

#same old EMInput module
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

# 01 - Print a table for the result of 2x + 5 if x is the value from 0 to 30 stepping by 3.
print(f"\n{hdiv} Question 1 {hdiv}")
print("Multiplication!")

for i in range(0,31,3):
    print(f"2({i}) + 5 = {2*i + 5}")

# 02 - Write a program that will print the line: “I am so smart, SMRT”,  then ask the user if they wish to continue.  
# The program stops when the user enters “n” and displays the number of times the line was printed
print(f"\n{hdiv} Question 2 {hdiv}")
print("Smartness!")

count = 1
print("I am so smart, SMRT")
while True: 
    while True:
        user_input = EMInput("Do you wish to continue? (y/n): ", "str").lower() #allows any typecase to be used
        if user_input not in ["y","n"]:
            print("Please enter y / n.") 
        else: break
    if user_input == "n":
        break
    else: 
        print("I am so smart, SMRT")
        count += 1 
print(f"The message was printed {count} times.")
        
# 03 - Write a simple Black Friday product purchasing calculator that factors in a 13% sales tax.
print(f"\n{hdiv} Question 3 {hdiv}")
print("well thats taxing")

items = [] #datastructure: item name, item cost, item amount
hst = 0.13
class item: #basic for readability, kind of unnecessary though
    cost = 0
    name = ""

#item input loop
while True: 
    item.name = EMInput("Give me the name of item you want to calculate the cost for!: ")
    item.cost = EMInput(f"How much is one {item.name}?: ", "float", "Please enter a number.")
    while True: #data verification to ensure >0 items to ensure that it makes sence.
        amount = EMInput(f"How many {item.name} ({item.cost:,.2f}/item) are you buying?: ", "int", "Please enter an integer number.")
        if amount > 0: 
            break
        else:
            print("Please enter an integer above 0.")
    items.append([item.name,item.cost,amount]) #appends the items to the items table with the datastructure listed above
    while True: #tool exit loop  
        status = EMInput("Do you want to stop this tool? (Y/N): ", "str").lower()
        if status not in ["y", "n"]: #input verification
            print("Please enter Y or N.")
        else: #if input is valid, break out
            break
    if status == "y": #only runs if the input above was valid and was y.
        break
#item display loop
total = 0 #cost total accumulator
counter = 1
for current_item in items: #for every [item_name, item_cost, amount] in items table:
    print(hdiv*3)
    print(f"Item #{counter}:{current_item[0]}\nPer-Item Cost:{current_item[1]}$\nQuantity Purchased:{current_item[2]}") #unpacks all 3 items
    print()
    print(f"Subtotal: {(current_item[1]*current_item[2]):,.2f} $") #item_cost * amount
    print(f"Tax: {(current_item[1]*current_item[2]*hst):,.2f} $") #item_cost*amount*tax (without +1)
    total += current_item[1]*current_item[2]*(1+hst) #item_cost*amount*tax (with +1)
    print(f"Current Total: {total:,.2f}$ ") #displays outcome above
    counter +=1 #counts item count.
print(hdiv*3)
print(f"Before Tax: {total/(1+hst):,.2f}$") #calculates the value before tax based on the sum
print(f"Taxed Amount: {(total/(1+hst))*hst:,.2f}$") #calculates the value of tax alone
print(f"Final Sum: {total:,.2f}$") #displays total

        