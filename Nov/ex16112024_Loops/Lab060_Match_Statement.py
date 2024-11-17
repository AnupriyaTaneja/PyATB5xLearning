# Match Statement : Similar to switch in Java
# match i/p and o/p
# Only available with  Python version > 3.10

# Syntax:
# match variable:
#   case pattern1:
#       # code block
#   case pattern2:
#       # code block


# Write a program to ask the user which browser they want to use for automation

broswer_name = input("Enter the browser name\n")
match broswer_name:
    case "firefox": # 'firefox' is different from 'FIREFOX' , so in case of latter o/p -> browser not found
        print("Starting Firefox!!")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _: # _ means default case : if nothing matches then this executes
        print("Browser not found!")
