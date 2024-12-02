# Frequency of Characters in a String
# Write a program to count the frequency of each character in a given string.
string = "automation"
string = input("Enter the input e.g automation:\n")


# Output should be -> {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}

char_count = {} # Created empty dictionary

# Logic building
# I/P - string e.g automation
# O/P -> dict  # {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}

for char in string:
    char_count[char] = char_count.get(char,0) + 1

print(char_count)

# Output:
# Enter the input e.g automation:
# automation
# {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}