a = 10 # Global variable

class Person:
    b = 11 # Instance variable -> belongs to this class

    def print_info(self):
        c = 20 # Local variable
        print(c) # For local variable , no need to use self
        print(self.b) # Self is needed to access the instance variable

        #a = "Hello"
        #print(a) # value will be Hello as local variable has more preference than the global variable

        global a
        print(a) # now it will print 10 as we used global keyword here

object_ref = Person()
object_ref.print_info()

