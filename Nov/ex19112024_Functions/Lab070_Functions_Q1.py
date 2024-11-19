# Create a program to sum of three number from the user input,
# if user doesn't enter any number', use default as 100, 200, 300

# Logic Building

a = int(input("Enter num1\n"))
b = int(input("Enter num2\n"))
c = int(input("Enter num3\n"))

def sum(num1=100, num2=200, num3=300):
#    print("Sum of numbers is ")
    return num1 + num2 + num3

result = sum(a,b,c)
print("Sum of first three numbers is ",result)

result_2 = sum()
print("Sum of next three numbers is ", result_2)
result_2 = sum(10)
print("Sum of next three numbers is ", result_2)
result_2 = sum(10,20)
print("Sum of next three numbers is ", result_2)
result_2 = sum(10,20,30)
print("Sum of next three numbers is ", result_2)
