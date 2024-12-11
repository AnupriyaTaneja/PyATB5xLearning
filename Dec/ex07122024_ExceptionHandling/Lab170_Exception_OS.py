import os

print(os.getcwd())
# Returns the current working directory
# Output -> C:\Users\91981\PycharmProjects\PyATB5xLearning\Dec\ex07122024_ExceptionHandling

# List files in the current directory
files = os.listdir('C:/Users/91981/PycharmProjects/PyATB5xLearning/Dec/ex07122024_ExceptionHandling')
print(f"Files in current directory: {files}")
#Output -> Files in current directory:
# ['Lab157_Exceptions.py', 'Lab158_Exceptions.py', 'Lab159_Exceptions.py', 'Lab160_Exceptions.py', 'Lab161_Exceptions.py', 'Lab162_Exceptions.py', 'Lab163_Exceptions.py', 'Lab164_Exceptions.py', 'Lab165_Exceptions_Fix.py', 'Lab166_Exceptions_try_except_syntax.py', 'Lab167_Exception.py', 'Lab168_Exception_Else_Finally.py', 'Lab169_Exception_Else_Finally.py', 'Lab170_Exception_OS.py', '__init__.py']


# Create a new directory
#os.mkdir('Test2') # Created a new directory/folder

# Check if a file exists
file_exist = os.path.exists("anu.txt")
print(file_exist) # Output -> False

# Prints name of the os
print(os.name) # posix == mac, nt - windows
#Output -> nt