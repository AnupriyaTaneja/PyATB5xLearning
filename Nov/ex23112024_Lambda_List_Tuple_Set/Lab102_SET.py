# SET
# Collection of Unique
# {} - parenthesis

list_of_unique_items = {1, 2, 3, 4, 4, 5, 5}
print(list_of_unique_items) # Set always returns unique elements

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1) # Converting list list1 to set set1
print(set1) # o/p -> {33, 21, 45, 45.2}

# Order of items printed from the set can be anything, i.e, set doesn't maintain the order

t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t) # Duplicates won't get removed in case of tuple
print(set(t)) # Duplicates will get removed now that tuple is converted to set
"""
Output:
'TheTestingAcademy', 'for', 'TheTestingAcademy')
{'TheTestingAcademy', 'for'}
"""