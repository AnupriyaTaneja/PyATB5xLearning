
# Sort a dictionary by its values in descending order
my_dict = {"a": 3, "b": 1, "c": 2}
# Order should be{b: 1 , c: 2 , a :3}

sort_by_value_asc = sorted(my_dict.values(), reverse= False)
print(sort_by_value_asc)


sort_by_value_desc = sorted(my_dict.values(), reverse= True)
print(sort_by_value_desc)
