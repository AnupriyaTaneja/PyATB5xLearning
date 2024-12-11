import os

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path + "/example.txt"
    print(full_path_file)

    # Read the file
    file = open(full_path_file)  # FileNotFoundError: [Errno 2] No such file or directory
except Exception as e:
    print("File Not found, fix the path or create a file")
finally:
    print("This code will be executed anyhow")

# Output:
# C:\Users\91981\PycharmProjects\PyATB5xLearning\Dec\ex07122024_ExceptionHandling
# C:\Users\91981\PycharmProjects\PyATB5xLearning\Dec\ex07122024_ExceptionHandling/example.txt
# File Not found, fix the path or create a file
# This code will be executed anyhow