i = 0
while i < 10:
    print(i)
    i = i + 1

# i = 0 , 0<10, o/p = 0 , i = 0+1 = 1
# i = 1 , 1<10, o/p = 1 , i = 1+1 = 2
# ......
# i = 9 , 9<10, o/p = 9 , i = 9+1 = 10
# i = 10 , 10<10 --> false -> exit the code

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

print("--------")

i = 0
while i < 5:
    print(i)
    i = i + 1

# Output:
# 0
# 1
# 2
# 3
# 4

print("--------")

i = 0
while i <= 5:
    print(i)
    i = i + 1

# Output:
# 0
# 1
# 2
# 3
# 4
# 5