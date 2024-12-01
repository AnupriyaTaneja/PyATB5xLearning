# Find the first non-repeating character in a string using sets.
# swiss -> w - Answer

def first_non_repeating_char (string):
    for char in string:
        if string.count(char) == 1:
            return char
    return None

print(first_non_repeating_char("swiss")) # w
print(first_non_repeating_char("pepper")) # r
print(first_non_repeating_char("dada")) # None
print(first_non_repeating_char("annusinha")) # u

print("-----------------------")
# Practicing printing values from a set
set1 = {10, 20, 30, 40, 50}
for i in set1:
    print((i) , end = " ")

