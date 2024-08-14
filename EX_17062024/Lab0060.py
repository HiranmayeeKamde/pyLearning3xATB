def greet():
    print("Hello")


greet()


####################################################################

def f1(a, b, c):
    print(a, b, c)
    return a + b + c


#    print("This code will not execute")

print("END")

# result = f1 (10, 20, 30)
# result = f1 (a=1, b=2, c=3)
result = f1(c=1, a=2, b=3)
# result =f1() -> Missing 3 args
print(result)

####################################################################
