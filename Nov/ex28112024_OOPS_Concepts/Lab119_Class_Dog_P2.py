class Dog:
    #Attributes

    # name = "Chow" -> in this case, name will be same for all objects created for this class when below is called
    # print(chow_ref.name) -> o/p -> Chow
    # print(mow_ref.name) -> o/p -> Chow

    name = None
    breed = None
    height = None
    weight = None

    def __init__(self):# Special function in a class. Will be automatically called when obj is created
        print("I will be called")


    #Behavior
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleeping")

    def talk(self):
        pass


#Object of the class Dog
chow_ref = Dog()
#Dog() -> Object
# chow -> Object ref

#Multiple objects can be created for a class
mow_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)