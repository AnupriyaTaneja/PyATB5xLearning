import os

file_name = "anu.txt"
content = "This is Anu's File ABC"

with open(file_name, "w") as file: # w is the mode with which the file can be opened-> w : write mode
    file.write(content)

with open(file_name, "r") as file: # read mode
    content2 = file.read()
    print(content2)

# os.chdir("Desktop")