def 123():
    print("Hi") # invalid as function name cant start with digit
# identifier rule is failed
#error-> identifier expected

def _123():  # identifier rule is valid, name can start with _
    print("Hi")


def _():
    print("Hi")


_()


def anu123():
    print("Hello")


def h():
    print("hello")
    print("I am part of h function ?")

print("Not a Part of Functions") # outside the function