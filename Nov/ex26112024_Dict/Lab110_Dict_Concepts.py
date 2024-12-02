# Create Dictionary from Two Lists

keys = ["name", "role", "experience"]
values = ["Aman", "SDET", 3]

my_dict = dict(zip(keys, values)) # Merged the 2 lists as a dictionary with 'zip' method
print(my_dict) # {'name': 'Aman', 'role': 'SDET', 'experience': 3}


# keys = ["name", "role", "experience"]
# values = ["Aman", "SDET"]

# my_dict = dict(zip(keys, values))

# Here dictionary gets created only for the matching number of items in the same order
# print(my_dict) # o/p -> {'name': 'Aman', 'role': 'SDET'}


# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict) # o/p -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(merged_dict.get("a")) # o/p -> 1

dict3 = {"e": 5, "f": 6}
merged_dict = merged_dict | dict3
print(merged_dict) # o/p -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dict4 = {"e": 5}
merged_dict = merged_dict | dict4
print(merged_dict) # o/p -> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

