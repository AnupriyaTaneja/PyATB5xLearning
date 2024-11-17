#Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = input("Enter the value of num1")
num2 = input("Enter the value of num2")
num1 = int(num1)
num2 = int(num2)
print("Quotient: ", num1//num2)
print("Remainder: ", num1%num2)
#or
print(divmod(15,2))

"""
Output:
Enter the value of num115
Enter the value of num22
Quotient:  7
Remainder:  1
"""