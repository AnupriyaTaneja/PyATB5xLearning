# Write a program to take a user age and let him know if he can go the club. Consider age limit as 21

#Logic Building Formula

# Step 1 - Figure out i/p and o/p
# user input i/p -> data type - int
# output o/p -> String message - if he/she can go

# Step 2 - Rough Logic (Brute Force Logic)
# age > 21 -> print can go
# age < 21 -> print can't go

# Step 3 - Write the logic

age = (input("Enter your age: \n"))
age = int(age)

if age >= 21:
    print("You are eligible to go to the club")
else:
    print("You are not eligible to go to the club")

# Step 4 - Check for the edge cases
#Negative or extremely high values or non-numeric values -> Program will break
#Age which is valid

"""
Enter your age: 
12223433894759347580860987097097083472347327427
You are eligible to go to the club

Enter your age: 
200
You are eligible to go to the club
"""

#Enter your age:
#ABC
#Traceback (most recent call last):
#  File "C:\Users\91981\PycharmProjects\PyATB5xLearning\Nov\ex14112024_Conditions_Loops\Lab043.py", line 16, in <module>
#    age = int(age)
#ValueError: invalid literal for int() with base 10: 'ABC'

"""
-----Even this is not right as no one has lived more than 130 years
Enter your age: 
200
You are eligible to go to the club
"""

# Step 5 - Optimize