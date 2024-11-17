# Program to find the max between two ( 3,4) → 4

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
# 1st way
# max_value = float(max(num1,num2))
# print("Maximum number is: " , max_value)

#2nd way
"""
if num1>num2 :
    max_value = num1
else:
    max_value = num2

print("Maximum number is: " , max_value)
"""

# 3rd way
#print("num1 is greater" if num1>num2 else "num2 is greater" )
print("Max number is: " , num1 if num1>num2 else num2)