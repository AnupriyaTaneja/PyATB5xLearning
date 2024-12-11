a = int(input("Ent the num1: ")) # ValueError: invalid literal for int() with base 10: 'anu'
b = int(input("Ent the num2: "))
c = a / b # ZeroDivisionError: division by zero
print("Result Div is ", c)

#Output:
#Ent the num1: anu
# Traceback (most recent call last):
#   File "C:\Users\91981\PycharmProjects\PyATB5xLearning\Dec\ex07122024_ExceptionHandling\Lab164_Exceptions.py", line 1, in <module>
#     a = int(input("Ent the num1: ")) # ValueError: invalid literal for int() with base 10: 'anu'
# ValueError: invalid literal for int() with base 10: 'anu'