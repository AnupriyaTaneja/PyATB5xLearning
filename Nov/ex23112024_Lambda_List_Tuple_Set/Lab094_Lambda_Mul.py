# Write a program to calculate even and odd

def find_even_odd(num) :
    if num % 2 == 0 :
        print("Even")
    else:
        print("Odd")

find_even_odd(5)

n = int(input("Enter a num\n"))
check_even_odd = lambda  n : "Even" if n % 2 == 0 else "Odd"

#print(check_even_odd(17))
#print(check_even_odd(10))
print(check_even_odd(n))