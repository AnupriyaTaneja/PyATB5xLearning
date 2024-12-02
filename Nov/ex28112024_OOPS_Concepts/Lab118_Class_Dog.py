class Dog:
    name = None
    breed = None
    height = None
    weight = None

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass


#Object of the class Dog
chow = Dog()
#Dog() -> Object
# chow -> Object ref

#Multiple objects can be created for a class
mow = Dog()
bow = Dog()
rancho = Dog()
