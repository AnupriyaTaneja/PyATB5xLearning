# before driving the scooty, add some extra security

def add_security(func): #this func name can be anything
# takes another function (drive_scooty() in this case) as an argument

    def wrapper(): #wrapper function name should always be the same
        print("1. Before the function is called.")
        print("2. Add helmet, dashcam, gloves, knee guards, licence")
        func() # calls driving scooty() function
        print("3. After function is called")
        print("4. Secure driving, leave all the items")
    return wrapper()

@add_security #@ is used to add the wrapper
def drive_ola_scooter():
    print("ola")

@add_security
def driving_scooty():
    print("Normal function")
    print("I am driving a scooty")