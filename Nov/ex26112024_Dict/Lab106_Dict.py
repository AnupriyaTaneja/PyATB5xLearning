# - Key and Value Pair.
# - A dictionary is an unordered, mutable, and indexed collection of key-value pairs in Python.
# - It is defined using curly braces {}.
# Where it will be used - API Automation( when we'll use JSON - Dict will be used)

my_dict = {
    "name": "Aman",
    "age": 34,
    "role": "SDET",
    "experience": 3
}
print(my_dict) # {'name': 'Aman', 'age': 34, 'role': 'SDET', 'experience': 3}
print(my_dict["age"]) # 34

my_dict["role"] = "Manual Tester"
print(my_dict) # {'name': 'Aman', 'age': 34, 'role': 'Manual Tester', 'experience': 3}

del my_dict["age"] # Deleting from dictionary using 'del' keyword
print(my_dict) # {'name': 'Aman', 'role': 'Manual Tester', 'experience': 3}

for key, value in my_dict.items():
    print(key, "->", value)
# Output:
# name -> Aman
# role -> Manual Tester
# experience -> 3

print("age" in my_dict) # False
print("role" in my_dict) # True