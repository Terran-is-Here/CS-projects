# Exercise #02

# 00 - example - your age
age = 16
print(f"I am {age} years old.")

# 01 - your middle name
middle_name = "Domingo"
print(f"My middle name is {middle_name}.")
# 02 - siblings you have
middle_name = "Lara, Lian, Lander, Luis"
number_of_cousins = 4
print(f"My {number_of_cousins} closest cousins ({middle_name}) are currently in the Philippines")
# 03 - your favorite color
favourite_color = "White"
print(f"My favourite color is {favourite_color}")

# 04 - place where you were born
birthplace = "Manila, Philippines"
print(f"I was born in {birthplace}")

# 05 - your favorite activity
favourite_activity = "Playing Rhythm Games"
print(f"My favourite activity is {favourite_activity}")

# 06 - your favorite Movie
favourite_movie = "Oppenheimer"
print(f"My favourite movie that I watched recently is {favourite_movie}")

# 07 - price of a slice of pizza (make up a number with a decimal)
pizza_cost = 12.52
print(f"A slice of pizza in the philppines costs {pizza_cost} Pesos.")
# 08 - print a sentence that combines 3 of the variables above into a sentence.
print(f"In {birthplace}, I wasnt able to watch {favourite_movie}, however the cost of Pizza was {pizza_cost} pesos, which is quite cheap.")

# 09 - Store a name and a message in two variables.
# print them out using string concatenation (+ sign) to join the two variables
m1 = "Jeff"
m2 = "likes watching skibidi toilet"
print(f"{m1} {m2}")

# 10 - Create a variable x and assign it the value 10.5, create a variable y, and assign it 4.
# Create a variable called multi and multiply x and y then print out the equation and multi variable answer.
x = 10.5
y = 4
multi = x*y
print(f"{x} * {y} = {multi}")

# 11 - Create a variable for age and total days alive. Write the code to determine roughly how many days you've been alive.
# total days will be an equation using 365 days in a year multiplied by your age)
age = int(input("How years old are you right now?"))
days_old = age*365
print(f"You are roughly {days_old} days old.")



# 12 - If the temperature outside today is –4 degrees Celsius, what is the equivalent temperature in Fahrenheit?
# (conversion formula is Fahrenheit = 9/5 * Celsius + 32.
temperature_celsius = int(input("How cold is it (in C) outside right now?: "))
farenheit_temperature = (9/5) * temperature_celsius + 32
print(f"It is currently {farenheit_temperature} Farenheit outside.")

# 13 - If you earn $10 per hour, what is your total payment if you work 15 hours per week?
money_income = 10
hours_worked = 15
print(f"Working {hours_worked} hours with an hourly income of {money_income}$ will give you a total income of {money_income*hours_worked}$")