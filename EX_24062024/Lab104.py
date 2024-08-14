# Filters in Python

# This is built in function filter()
# allow you to filter element in the list, tuple, set.

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# filter on the above -> even number
# new_list_Even = [2,4,6,8,10]
def is_even(n):
    return n % 2 == 0


new_num_even = filter(is_even, number)
print(list(new_num_even))
