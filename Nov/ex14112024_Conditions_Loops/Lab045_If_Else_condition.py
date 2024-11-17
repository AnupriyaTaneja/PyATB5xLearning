# Problem to find maximum of 2 numbers

# Logic Building Formula
# 1. user inputs -> two float
# 2. o/p -> which ever is greater

num1 = float(input("Enter num1\n"))
num2 = float(input("Enter num2\n"))

if num1 >= num2:
    print("Max is ", num1)
else:
    print("Max is ", num2)

# Edge cases
# num1 = num2 -> already handled
# String -> ABC , ten -> try and except : will learn in future
# negative values -> already handled
