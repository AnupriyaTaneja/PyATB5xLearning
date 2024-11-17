# Program - if age > 18 - allowed to vote
# else -> not allowed to

user_age = int(input("Enter your age \n"))

if user_age > 18 :
    print("you are eligible to vote")
else :
    print("you are not eligible to vote")

#or

print("you are eligible to vote" if user_age > 18 else "you are not eligible to vote")

# or

print("you are eligible to vote" if int(input("Enter your age \n")) > 18 else "you are not eligible to vote")

# It is not recommended to write one-liner codes and hence the 1st option is most advisable