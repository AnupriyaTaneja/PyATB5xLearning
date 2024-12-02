# Count vowels in an input string
input_string = "hello, world!'\'"
# a,e,i,o,u

vowels = "aeiouAEIOU"

vowels_count = 0
consonants_count = 0
symbol_space_count = 0

for characters in input_string:
    if characters in vowels:
        vowels_count = vowels_count + 1
    elif characters in (" ", "@", "!", ",", "#", "$", "%", "^", "&", "*", "(", ")", ";", "{", "}", "[", "]", "'", ".", "/", "<", ">", "_","-", "+", "=", "|", "?", "'\'"):
        symbol_space_count = symbol_space_count + 1
    else:
        consonants_count = consonants_count + 1

print(vowels_count) # 3
print(consonants_count) # 7
print(symbol_space_count) # 5


