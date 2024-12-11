class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        print("3BHK")


s = Son()
s.home()

f = Father()
f.home()