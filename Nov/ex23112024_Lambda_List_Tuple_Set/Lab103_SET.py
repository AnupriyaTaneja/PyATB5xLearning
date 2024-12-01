set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)
# Output : {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)
# Output : {4, 5}

my_set = set1.difference(set2)
print(my_set) # Output : {1, 2, 3}
my_set = set2.difference(set1)
print(my_set) # Output : {8, 6, 7} -> Remember set has no order so sorting of items is not done by default


