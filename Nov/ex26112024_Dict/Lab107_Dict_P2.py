student_info = {
    "name" : "Anu",
    "age" : 34,
    "address" : "Noida"
}

print(student_info["name"]) # Anu
print(student_info["age"]) # 34
print(student_info["address"]) # Noida

student_info["age"] = 100
print(student_info["age"]) # 100

student_infor2 = dict(name="A", age=67, address="KA")

# Dictionary within dictionary
student_infor1 = {
    "name": "A",
    # "age": 65,
    "age": 67,
    "address": { # Dictionary within dictionary
        "home_address": "ND",
        "office_address": "KA"
    }
}

