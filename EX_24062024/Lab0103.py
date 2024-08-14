my_dict = {'a': 1, 'b': 2, 'c': 3}
# itrate
# To find key
for k,v in my_dict.items():
    if k == 'b':
        print("Key with the name b is found")

op = 'b' in my_dict
print(op)