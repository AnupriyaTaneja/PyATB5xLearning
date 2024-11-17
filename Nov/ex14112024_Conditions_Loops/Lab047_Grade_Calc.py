# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

# Logic Building Formula

# i/p : user inputs -> score or marks -> int
# o/p : str -> A or B....

score = int(input("Enter your score:\n"))

if score >= 90 and score <= 100:
    print("Your grade is: ", "A")
elif score >= 80 and score <= 89:
    print("Your grade is: ", "B")
elif score >= 70 and score <= 79:
    print("Your grade is: ", "C")
elif score >= 60 and score <= 69:
    print("Your grade is: ", "D")
elif score > 100 or score <= -1:
    print("You are a superman! You can't get a grade!! ")
else:
    print("Your grade is: ", "F")
