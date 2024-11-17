# FizzBuzz Test:
# Write a program that prints numbers from 1 to 100.
# However, for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."
# use for and if both

"""
for i in range(1,101,1):
    if i % 3 == 0 :
        if i % 5 == 0 :
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i % 5 == 0 :
        if i % 3 == 0 :
            print("FizzBuzz")
        else:
            print("Buzz")
    else :
        print(i)
"""

for i in range(1,101,1):
    if ((i % 3 == 0) and (i % 5 == 0)):
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
            print("Buzz")
    else:
        print(i)