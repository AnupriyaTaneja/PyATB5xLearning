class Father:
    key = "2BHK"

    def car(self):
        print("Father has a car -> Alto")
        print(self.key)

class Son(Father):#Single Inheritance
    key2 = "3BHK"

    def suv(self):
        print("Son has MG Hector, Black")
        print(self.key2)

father_obj = Father()
father_obj.car()
print("----------------")
son_obj = Son()
son_obj.suv()
son_obj.car()
print(son_obj.key2)
print(son_obj.key)