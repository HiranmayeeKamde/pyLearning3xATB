# *args -> is similar to [] List which contain n no of arguments
def print_arguments(*args):
    for i in args:
        print(i,end = "***")
print_arguments("Ekanth", "varsha", 23, 110.3)

########################################################################

# *arg -> List
a = ["pramod","lucky","sumit"]
for i in a:
    print(i)
########################################################################

for i in range(1,10):
    print(i)