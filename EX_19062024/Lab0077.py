# Odd Even Number

def find_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

l = find_even_odd(5)
print(l)

# Using lambda function

check_even_odd = lambda num: "even" if num% 2 == 0 else "odd"
print(check_even_odd(6))