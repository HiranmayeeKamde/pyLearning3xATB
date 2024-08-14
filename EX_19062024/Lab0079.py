# List : List is collection of Items (duplicate is allowed)

my_list = [1, 2, 3]
my_list2 = [1, True, "Hiranmayee", 12.34]

# Indexing
my_list[1] = 20
print(my_list)

# append : add in the end of list
my_list.append(4)
print(my_list)

# extend() : it will extend the list
my_list.extend([4, 5, 6])
print(my_list)

# insert(index, value) : add value at particular index
my_list.insert(1, "h")
print(my_list)

#remove(value) : remove particular value
my_list.remove("h")
print(my_list)

# copy() : copy the list
my_copy_list = my_list.copy()
print(my_copy_list)

# clear() : deleting the list
my_list.clear()
print(my_list)

# What is the 3rd index in my_list?
#print(my_list[3]) #IndexError: list index out of range

my_list = [100, 2, 3.9, 0.4, 5]
# sort() : sorting the list
my_list.sort()  # This is sallow copy
print(my_list)

# reverse() : reverse the list
my_list.reverse()
print(my_list)


