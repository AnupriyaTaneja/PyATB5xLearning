for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        print("No o/p")

"""
Output:
No o/p
No o/p
No o/p
No o/p
No o/p
No o/p
6
No o/p
No o/p
No o/p
"""

print("----------------------------")

for i in range(0, 10, 1):
    print(i)
    if i == 6:
        break
"""
Output:
0
1
2
3
4
5
6
"""

print("----------------------------")

for i in range(0, 10, 1):
    if i == 6:
        print(i)
        break
    else:
        print("No o/p")

"""
Output:
No o/p
No o/p
No o/p
No o/p
No o/p
No o/p
6
"""