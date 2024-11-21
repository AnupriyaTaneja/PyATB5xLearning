def outer_function():
    var1 = 30  # local

    def inner_function():
        #var2 = 90
        print("Inner func1" ,var1)#Outer func variables can be used by inner functions,but vice versa isn't possible

    def inner_function2():
        print("Inner func2" ,var1)

#for both inner functions var1 is a global variable, so these both can access this
    inner_function() # Step 2. call inner functions inside the outer function
    inner_function2()
    #print(var2) #local variable cant be accessed outside the function


outer_function() # Step1 . Call the outer function
#inner_function() #cant be called outside
#-  Outer functions - vars can be used by the inner functions.
