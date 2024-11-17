# Write a program to take a user age and let him know if he can go the club. Consider age limit as 21

age = int(input("Enter your age: \n"))
if age >= 21:
    print("You are eligible to go to the club")
else:
    print("You are not eligible to go to the club")
