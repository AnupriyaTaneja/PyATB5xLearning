class Calc:

    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

object_ref = Calc()
a = float(input("Enter the first num: "))
b = float(input("Enter the second num: "))

output_sum = object_ref.sum(a,b)
output_sub = object_ref.sub(a,b)
output_mul = object_ref.mul(a,b)
output_div = object_ref.div(a,b)

print(output_sum, output_sub, output_mul, output_div)

"""
Output:
DC
Enter the first num: 34
Enter the second num: 2
36.0 32.0 68.0 17.0
"""