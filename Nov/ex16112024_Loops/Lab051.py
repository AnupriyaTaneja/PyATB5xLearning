for i in range(1, 10, 2):
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9

# giving start and step is optional
# default values of start =0 and step = 1
print("------------------")
for i in range(10):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# print("------------------")
#for i in range():
#    print(i)
# output:
# Traceback (most recent call last):
#   File "C:\Users\91981\PycharmProjects\PyATB5xLearning\Nov\ex16112024_Loops\Lab051.py", line 27, in <module>
#     for i in range():
#              ~~~~~^^
# TypeError: range expected at least 1 argument, got 0

print("------------------")
for i in range(-10,-1):
    print(i)
# output:
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2

print("------------------")
for i in range(-10,-1, 2):
    print(i)
# output:
# -10
# -8
# -6
# -4
# -2

print("------------------")
for i in range(-1, -10, -1):
    print(i)
# output:
# -1
# -2
# -3
# -4
# -5
# -6
# -7
# -8
# -9