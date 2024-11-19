def first_part_last_name():
    pass  # # in future I will complete this functions


def greet_to_all_of_you():
    print("Hello, Everyone")


def greet():
    print("Yes")
    greet_to_all_of_you() # Calling earlier function inside the new function

greet() # calling second function outside

# So output will be:
# Yes # greet() function will be called first so the first line of code in this function is called first
# Hello, Everyone -> as this was called as the second line of code in greet() function