def say_hello():  # No Return Type
    print("Hello")


say_hello()


def say_hello_arg(name):
    print("Hello", name)


say_hello_arg("Soumya")
say_hello_arg("John")


#############################################
def say_hello_arg_default(name="hira"):  # No Return type with default arg
    print("Hello", name)


say_hello_arg_default()
say_hello_arg_default("John")
say_hello_arg_default(name="Soumya")


###############################################
def sum_return(a, b):  # Argument +return
    return a + b


result = sum_return(2, 3)
result1 = sum_return(3,8)
print(result)
