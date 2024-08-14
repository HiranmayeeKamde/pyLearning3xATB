def sum_two(a,b):
    return a+b


o = sum_two(2, 3)
print(o)

# Using Lambda function -> for one liner without def keyword
output_function = lambda a,b : a+b
print(output_function(8,9))

# Note : lambda expression is not possible for more than one liner
