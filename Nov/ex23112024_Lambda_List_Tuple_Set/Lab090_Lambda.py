#Lambda

def triple_num(num):
    return num**3

result = triple_num(2)
print(result)

#Using Lamda
result_l = lambda num: num ** 3
print(result_l(2))

#multiple statements not allowed with lambda