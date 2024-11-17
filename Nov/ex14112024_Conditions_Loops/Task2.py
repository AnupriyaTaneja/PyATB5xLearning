"""
Checking for a Leap Year , 2024 → Yes
Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.
"""

year = int(input("Enter the year: "))
print("Divisible by 4? : ", bool(year % 4 == 0))
print("Divisible by 100? : ", bool(year % 100 != 0))
print("Divisible by 400? : ", bool(year % 400 == 0))

if ((year % 4 == 0) & (year % 100 != 0)) or (year % 400 == 0):
    print(year, "  is a leap year")
else:
    print(year, "  is not a leap year")
