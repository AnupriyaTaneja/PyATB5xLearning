class Person:

    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name


anu = Person ("Anu")
priya = Person ("Priya")

print(anu.name)
print(priya.name)

print("Who is walking?" , anu.walk())
print("Who is walking?" , priya.walk())

# Output:
# Anu
# Priya
# Who is walking? Anu
# Who is walking? Priya