# Program to find maximum of 3 numbers

# Logic Building Formula
# i/p -> num1, num2, num3 -> int
# o/p -> int or string of max num

# Logic ? if else - used for only 1 condition
# for more than one condition : use if elif else

# Syntax:
# if condition 1:
#   print("do 1")
# elif condition 2:
#   print("do 2")
# elif condition 3:
#   print("do 3")
# else:
#   print("do for else")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

# Rough Logic : num1>num2 and num1>num3 : o/p -> num1

if (num1 > num2) and (num1 >= num3):
    print("Max is: ", num1)
elif (num2 >= num1) and (num2 >= num3):
    print("Max is: ", num2)
else:
    print("Max is: ", num3)
