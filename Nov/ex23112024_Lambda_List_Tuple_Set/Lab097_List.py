my_list = [1, 2, 3]

# Indexing
print("element at the index 0 - ", my_list[0])
print("element at the index 1 - ", my_list[1])
print("element at the index 2 - ", my_list[2])

# append() - # Append object to the end of the list.
my_list.append(4)
my_list.append(5)
print(my_list)

# extend() - Append a new list
my_list.extend([7, 8, 10, 9])
print(my_list)

# insert()
my_list.insert(1, "Taneja")
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)

my_list[1] = "Anu"
print(my_list)

# remove()
my_list.remove("Anu")
print(my_list)

print(" --------------------------")
print(" --------------------------")

my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Taneja")
my_list.remove("Taneja")

# if list has items with multiple data types then sorting won't happen, hence we removed string above
my_copy_list.sort()

print(my_list) # since we only sorted the copied list, hence the original list is not sorted
print(my_copy_list)