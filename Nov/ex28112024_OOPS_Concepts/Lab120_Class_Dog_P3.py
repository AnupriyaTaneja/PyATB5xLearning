class Dog:
    #Attributes

    name = None
    breed = None
    height = None
    weight = None

    def __init__(self, name, breed):
        print("Parameterized Constructor")
        self.name = name
        self.breed = breed

    #Behavior
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleeping? " + self.name)

    def talk(self):
        pass


#Object of the class Dog
chow_ref = Dog("Chow", "Corgi") #-> first function to be called now is the constructor
mow_ref = Dog("Mow", "Husky")

print(chow_ref.name)
print(chow_ref.breed)
print(mow_ref.name)
print(mow_ref.breed)
# Output:
# Chow
# Corgi
# Mow
# Husky

#print(chow_ref.name, chow_ref.breed)# O/p -> Chow BB

chow_ref.sleep()
mow_ref.sleep()
# Output:
# Who is sleeping? Chow
# Who is sleeping? Mow

print(id(chow_ref))
print(id(mow_ref))
# Output:
# 2022564199600
# 2022567342992
