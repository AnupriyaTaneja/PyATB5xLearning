class A:
    def method(self):
        print("Method A")

class B:
    def method(self):
        print("Method B")

class C(B,A):
    pass

c_obj = C()
print(c_obj.method())

# Output:
# Method B
# None