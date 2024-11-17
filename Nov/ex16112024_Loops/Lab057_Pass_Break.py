for i in range(0, 10, 1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass
# pass is a placeholder statement that does nothing
# It's used when a statement is syntactically required but no action is needed.

# |i| |Condition|     |o/p|
# |0| |0==5 or 0==6-> False| |o/p -> Nothing will be printed|
# |1| |1==5 or 1==6-> False| |o/p -> Nothing will be printed|
# |2| |2==5 or 2==6-> False| |o/p -> Nothing will be printed|
# |3| |3==5 or 3==6-> False| |o/p -> Nothing will be printed|
# |4| |4==5 or 4==6-> False| |o/p -> Nothing will be printed|
# |5| |5==5 or 5==6-> True| |5|
# |6| |6==5 or 6==6-> True| |6|
# |7| |7==5 or 7==6-> False| |o/p -> Nothing will be printed|
# |8| |8==5 or 8==6-> False| |o/p -> Nothing will be printed|
# |9| |9==5 or 9==6-> False| |o/p -> Nothing will be printed|
# |10| |10==5 or 10==6-> False| |o/p -> For loop Exit|

# Output:
# 5
# 6