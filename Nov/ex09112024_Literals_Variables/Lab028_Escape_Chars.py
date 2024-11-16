#Escape Sequence

# Diff between " " & ''
c = 'C'
c1 = "C"

dir = 'C:\Anu\n.txt'
dir1 = "C:\Anu\n.txt"
print(dir) #SyntaxWarning: invalid escape sequence '\A'
print(dir1) #SyntaxWarning: invalid escape sequence '\A'

# r (or raw string) is resolving this issue
dir = r'C:\Anu\n.txt'
dir1 = r"C:\Anu\n.txt"
print(dir)
print(dir1)

