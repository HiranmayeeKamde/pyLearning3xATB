letters = ['a','b','c','d','e','j','o','u']
# this will work 
# Find the vowels

def filter_vowels(letter):
    vowels = ['a','e','i','o','u']
    return letter in vowels

result =filter_vowels('p')
print(result)

filter_words = filter(filter_vowels,letters)
print(list(filter_words))