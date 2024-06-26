# Fibonaci Series
# Fibonaci series means next number is the summation of previous two numbers.
# 0,1,1,2,3,5,8,13,21,34,55,89,144,...
num = int(input("Enter the number :"))
n1 = 0
n2 = 1

for i in range(1, num + 1):
    nth = n1 + n2
    n1 = n2
    n2 = nth
    print(nth)
