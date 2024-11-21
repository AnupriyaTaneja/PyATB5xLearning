pb_global_b = 12  # global variable


def my_function():
    pb_a = 10  # local variable
    print(pb_a)
    print(pb_global_b)


# my_function() # Output -> 10 , 12

# print(pb_a) # error -> NameError: name 'pb_a' is not defined

print(pb_global_b)
my_function()

# Output:
# 12
# 10
# 12
