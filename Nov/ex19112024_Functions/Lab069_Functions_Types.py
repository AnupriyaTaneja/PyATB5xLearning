# User Defined
# 1. They can't return -> non-return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments


# 1. They can't return -> non-return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")

greet()


# 2. # No Return Type and with Argument/ Param
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Anu")


# 3. No Return Type and with Default Argument ( # positional argument)
def say_hello_default_arg(name="Anupriya"):
    print("Hello", name.upper())


say_hello_default_arg("Taneja") # returns value which is passed explicitly
say_hello_default_arg() # else uses default value Anupriya


def multiple_args(name1="A", name2="B"):
    print("Mul -> ", name1, " and " ,name2)


multiple_args() # as no args passed so, uses default values A and B
multiple_args("XYZ", "ABC")
multiple_args("PQR")  # takes this as name1 or first arg by default
multiple_args(name1="Anu")
multiple_args(name1="Priya", name2="Taneja")
multiple_args(name2="Taneja")


# 4. Argument + return Type


def sum_of_two(a, b):
    return a + b


result = sum_of_two(4, 56)
print(result)


def sum_of_two_number_with_default(num1=100, num2=200):
    print("I will sum the two numbers!")
    return num1 + num2

result = sum_of_two_number_with_default(num1=34, num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)