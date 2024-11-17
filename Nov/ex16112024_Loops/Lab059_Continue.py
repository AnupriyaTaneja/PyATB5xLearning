for number in range(10) :
    if number % 2 == 0:
        continue
    else:
        print(number)

# |i| |Condition|       |o/p|
# |0| |0%2 ==0 -> True| |continue : skip no o/p|
# |1| |1%2 ==0 -> False| |1|
# |2| |2%2 ==0 -> True| |continue : skip no o/p|
# |3| |3%2 ==1 -> False| |3|

# Output: # All odd numbers
# 1
# 3
# 5
# 7
# 9

# continue and pass are same, but pass can be used in functions, statements, classes and objects also