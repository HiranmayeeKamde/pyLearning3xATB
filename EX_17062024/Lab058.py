# Function
# Block of code - which can executed or reused.
# Define
# Call

# Builtin function - builtins.py - file (Python 3 setup)
# Which are created by the Python Contributers
result = max(2, 3)


# User Define function
# 1. They can return something
# 2. They can not return -> non-return
# 3. They have parameter
# 4. They don't have paramter / arguments
############################################################################
# Example 3 : No return type and No Paramter / Argument
def say_hello():  # No return type and No Paramter / Argument
    print("Hello")


result1 = say_hello()
print(result1)  # None

############################################################################
# Example 2 : No return type but have parameter
def say_hello_arg(name):
    print("Hello ", name)

result2 = say_hello_arg("Rajesh")
print(result2) # None
say_hello_arg("Ramesh")

############################################################################
# Example 3 : No Return type with default parameter
def say_hello_arg_default(name = "Hiranmayee"):
    # write a code
    print("Hello", name)

say_hello_arg_default() # No ardument
say_hello_arg_default("Pramode") # Way 1 : with argument
say_hello_arg_default(name = "Varsha") # Way 2 : with specific value
# Here default value will not be used "Varsha" will be used

############################################################################
# Example : Return type with argument
def sum_number(num1, num2):
    return num1 + num2

sum_number(4,6)
result = sum_number(num1=6, num2=9)
result = sum_number(num2=0, num1=7)
print(result)

