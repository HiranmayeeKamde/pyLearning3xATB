# Important Question :

# Lambda Expressions: To do the task in one line

def double_my_salary(salary):
    return salary * 2


new_salary = double_my_salary(100)
print(new_salary)  # Output: 200

# Using Lambda Expressions:
# lambda arg_name : return value
f_double_salary = lambda salary: salary * 2
print(f_double_salary(100))