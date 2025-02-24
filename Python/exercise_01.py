# Exercise #01

subjects = ["SPH3UR","AWQ3MR", "ICS3UR", "SCH3UR"]
rooms = ["248", "124", "165","250"]
timeslots = ["08:10 - 09:25", "09:30 - 10:45", "11:30 - 12:45", "12:50 - 14:05"]

# 01 - Write a Python program to print your first and last name.
print("Pablo Luis Cauton")

# 02 - Write a Python program to print your daily schedule.
print("\nDaily Schedule")
for i in range (1,5): 
    print(f"Period {i}: {subjects[i-1]} @ {rooms[i-1]} ({timeslots[i-1]})")


# 03 - Print a string that includes double quotation marks (") inside the string.
print("\"Hello World\" was such a 2008 first line of code. We need something for the modern age")

# 04 - Print a string that includes an apostrophe (') inside the string.
print("'Hey, why did you surround me with single quotations >:('")

# 05 - Write a Python program to add 56789 and 1234 (Do not use quotes; let Python do the math!).
print(f"56789+1234 = {56789+1234}")

# 06 - Write a Python program to multiply 888 by -567. (Do not use quotes; let Python do the math!).
print(f"888*-567 = {888*-567}")

# 07 - Write a Python program to divide 961 by 31. (Do not use quotes; let Python do the math!).
print(f"961/31 ={961/31}")

# 08 - Write a Python program to find the remainder when dividing 1003 by 10. (Do not use quotes; let Python do the math!).
print(f"1003%10 = {1003%10}")

# 09 - Write a Python program to multiply the numbers 0 to 9 by 7. (Do not use quotes; let Python do the math!).
for i in range(0,10):
    print(f"{i} * 7 = {i*7}")

# 10 - Print your name, grade, and school on three separate lines using a single print() statement with escape characters.
print("Pablo Luis Cauton \n Grade 11 \n St.Paul High School")

# 11 - Calculate the average of 87, 79, and 92. (Hint: Add the numbers and divide by how many there are!) 
print("Average of 87, 79 and 92 is:", (87+79+92)/3)

# 12 - Write a Python program to print the numbers 1, 2, 3, 4, 5 on the same line, separated by a -.
# ??? i mean, i get doing it by the quotations but the simplest way works the best!
print("1-2-3-4-5")

# 13 - Print the following sentence, but ensure there is a tab space (\t) before the word "Python": 
print("The sentence given here didnt appear, but atleast \t \"Python\" was here to save the day!")

# 14 - Create an ASCII-style drawing using escape characters (\t, \n, quotes, and backslashes). Use at least 5 print() lines to create a house, smiley face, or simple pattern.

ascii_art=["======= ", "|  I  | ","|=<o>=| " ,"|  I  | ", "======= "]
barrel_count = int(input("How rows of 5 barrels (idk whats in them) do you want to be shown on your CLI?: "))
barrels_printed = 0
while barrels_printed < barrel_count: 
    for i in ascii_art:
        print(i *5)
    barrels_printed += 1

print(f"\n Here are {barrel_count * 5} barrels, free of charge!")