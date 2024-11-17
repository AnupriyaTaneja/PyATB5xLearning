"""
Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sides are equal),
isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""

s1 = int(input("Enter side1: "))
s2 = int(input("Enter side2: "))
s3 = int(input("Enter side3: "))

if s1 == s2 and s1 == s3:
    print("This is an equilateral triangle")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")