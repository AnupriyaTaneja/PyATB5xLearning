#Hierarchial Inheritance

class Father:

    def BHK1(self):
        print("1BHK")

class A(Father):

    def BHK2(self):
        print("2BHK")

class B(Father):

    def BHK3(self):
        print("3BHK")

class C(Father):

    def BHK1(self):
        print()

a_obj = A()
a_obj.BHK1()
a_obj.BHK2()

b_oj = B()
b_oj.BHK1()
b_oj.BHK3()
# b_obj.BHK2() # This belong to A

c_obj = C()
c_obj.BHK1() # Only Father house