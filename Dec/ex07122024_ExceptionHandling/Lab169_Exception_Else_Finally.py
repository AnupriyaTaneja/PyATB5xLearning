
try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1 / num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("Output is ", result)
finally:
    print("This code will be always executed.!")

#Output:
# Enter a Number 1
# 2
# Enter a Number 2
# str
# invalid literal for int() with base 10: 'str'
# This code will be always executed.!