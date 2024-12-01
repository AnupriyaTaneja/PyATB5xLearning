t = tuple ()
print(t)

# Convert list to tuple
t1 = tuple (["ms", "anupriya", "taneja"])
print(t1)

tup1 = ("A", "B")
tup2 = ("C", "D")
new_tuple = (tup1, tup2)
print(new_tuple) # Tuple within Tuple -> output: (('A', 'B'), ('C', 'D'))
print(new_tuple[0]) # ('A', 'B')
print(new_tuple[0] [0]) # A
print(new_tuple[1] [1]) # D
