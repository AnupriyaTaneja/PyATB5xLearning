# my_list = [1, 2, 2, 3, 4, 4, 5]
# Remove duplicates from a list using a set.
# Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 2, 3, 4, 4, 5]

result_set = set(my_list)
print(result_set) # Output -> {1, 2, 3, 4, 5}
print(list(result_set)) # Converting back to list again, final output -> [1, 2, 3, 4, 5]