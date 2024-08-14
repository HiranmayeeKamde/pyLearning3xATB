# Map() :
# 1. Take each item from the list
# 2. execute the function on it
# 3. retuen same number of elements (list)

my_list = [1, 2, 3, 4, 5]
def double(x):
    return x+2

double_list = list(map(double,my_list))
print(double_list)

# Note : map() is a amazing thing without using for loop in a function you can execute a function directly
# without using for loop is you want to execute each an item you can directly use map

# Using lambda expression
my_lambda_func = lambda x: x*2
result = my_lambda_func
print(result)