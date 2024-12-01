# List - Collection  of items
# grocery List -  butter, bread, banana, paneer.
# 10th marks - 90,91,92, 78, 56

"""
- Collection of Items.
- Duplicate are allowed.
- Multiple different data types are allowed.
- Stored with the Index -> 0 to len-1
-  List is Mutable in nature
"""

my_list = [1, 2, 3]  # Same type of data (int)
my_list2 = [1, True, "Pramod", 12.34]

print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
# print(my_list[4]) # list index out of range

my_list[0] = "Anu"
my_list[1] = "Priya"
my_list[2] = "Priya2"
print(my_list)

print(" -- ")

for item in my_list2:
    print(item)

print(" --- ")
#there is no need to call range function in case of iterating through a list as range also returns a list in itself
# , hence the previous option is better
for i in range(1, 5): # range( start, stop-1)
    print(i ,end=" ")

# range(1,5) -> returns List [1,2,3,4]
