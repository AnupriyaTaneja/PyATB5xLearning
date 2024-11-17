# Write a Python program to calculate the area of a circle
# given its radius using the formula area=π×r^2 ( Take pie as 3.14)
# area = π * r ^ 2 (Take π as 3.14)
import math

# Logic Building Formula

# Step 1
# Figure out all inputs and outputs
# input -> r -> data type -> float
# pi = 3.14
# power -> use pow function or ** operator
# o/p -> float -> area , print area

# Step 2
# rough logic = area  = 3.14 * pow (r,2)

# Step 3
radius = float(input("Enter radius of the circle\n"))
print(radius)
area = 3.14159265359 * (radius ** 2)
print("Area of the circle is = ", area)
print(f"Area of the circle is {area:.2f} ")  # f -> formatting , in this ex value is reduced to 2 decimal places

# * -> mul
# ** -> power

print("-----------")

# 0r

print(math.pi)
print(math.pow(radius, 2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is = ", area)

print("-----------")

# 0r

# print("Area of circle is : " , float(3.14 * float(input("Enter radius of the circle\n")) ** 2))


import math
print(math.pi)
print(math.pow(2,2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))

"""
Output:

Enter radius of the circle
10
10.0
Area of the circle is =  314.159265359
Area of the circle is 314.16 
-----------
3.141592653589793
100.0
Area of the circle is =  314.1592653589793
-----------
3.141592653589793
4.0
0.8939966636005579
-0.4480736161291701
-1.995200412208242
"""