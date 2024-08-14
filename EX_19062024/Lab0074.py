# List : collection of items

number = [1, 2, 3, 4, 5]


def do_something(Hiranmayee_list):
    Hiranmayee_list.append(6)  # Update list or add
    Hiranmayee_list[0] = 100  # Modified list
    return Hiranmayee_list


l = do_something(number)
print(l)
