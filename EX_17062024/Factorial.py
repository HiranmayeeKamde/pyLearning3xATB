# Factorial
# n =5
# result = 5*4*3*2*1

#############################################################
# Direct function is  "math.factorial(n)"
#############################################################

n = int(input("Enter the number :"))
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
print("The factorial of", n, "is :", factorial)


#############################################################
# By using while loop
#############################################################

n = int(input("Enter the number :"))
factorial = 1

while n > 0:
    factorial = factorial*n
    n = n-1

print("The factorial of", n, "is :", factorial)
