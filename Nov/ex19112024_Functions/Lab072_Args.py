def mul_args(*args):
    # *args - multiple arguments possiple at runtime
    print("---------")
    for i in args:
        print(i)


mul_args("A")
#print("---------")
mul_args("A","B")
#print("---------")
mul_args("A","B",10, 50, 7.5, "l")
