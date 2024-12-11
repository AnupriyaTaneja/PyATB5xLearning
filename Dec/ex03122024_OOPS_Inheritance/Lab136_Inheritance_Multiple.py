# Multiple Inheritance is not supported in Java but Python supports it


class Father:

    def home(self):
        print("Father home")

    def father_money(self):
        return  5

class Mother:

    def home(self):
        print("Mother home")

    def mother_money(self):
        return 2

class Son (Father, Mother):

    def print_info(self):
        print("Son")

son_obj = Son()
son_obj.print_info()
print(son_obj.father_money())
print(son_obj.mother_money())
son_obj.home() # here home is same name in both classes so whatever class is inherited first, then its method is called.
