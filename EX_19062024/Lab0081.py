# We want to double the item in the list
my_list = [1, 2, 3, 4, 5]
# print(my_list*2)

temp_list = []
for item in my_list:
    temp_list.append(item*2)

print(temp_list)

# Using lambda expression
my_lambda_func = lambda : temp_list.append(item*2) for i in my_list

print(my_lambda_func(my_list))