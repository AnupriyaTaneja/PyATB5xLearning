# Create a class, with public and private variable and method to access them outside

class Child:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.__mobile = 123456

    def showInfo(self):
        print(self.name)
        print(self.dob)
        print(self.__showMobile())

    def __showMobile(self):
        return self.__mobile

c1 = Child("ABC", "765420")
c1.showInfo()
