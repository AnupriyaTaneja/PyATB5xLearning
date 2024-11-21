public_toilet ="PB"

def home():
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet)
    #print(private_toilet) #private variable , so cant be used

print(public_toilet)
#print(private_toilet)#private variable , so cant be used

home()

# local variables have more preference as compare to public variables.`
