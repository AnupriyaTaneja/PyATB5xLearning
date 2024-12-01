cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities) # O/p -> True
print("New Delhi" in cities) # O/p -> False

t = (12, 34, 56)
# t.append(12) # AttributeError: 'tuple' object has no attribute 'append'
# Appending to a tuple isn't allowed, so we can convert it to a list and then append

my_list = list(t) # Converted tuple t to list my_list
my_list.append(4)
t = tuple(my_list) # Converted back the list my_list to tuple t
print(t)

ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)