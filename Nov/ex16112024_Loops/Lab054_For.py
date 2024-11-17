for i in range(0, 10):
    if i == 5:
        print("Five")
    else:
        print(i)

# |i| |Condition|     |o/p|
# |0| |0==5 -> False| |0|
# |1| |1==5 -> False| |1|
# |2| |2==5 -> False| |2|
# |3| |3==5 -> False| |3|
# |4| |4==5 -> False| |4|
# |5| |5==5 -> True| |Five|
# |6| |6==5 -> False| |6|
# |7| |7==5 -> False| |7|
# |8| |8==5 -> False| |8|
# |9| |9==5 -> False| |9|
# |10| |10==5 -> False| |For loop finished : o/p -> Exit|


"""
Output:
0
1
2
3
4
Five
6
7
8
9
"""