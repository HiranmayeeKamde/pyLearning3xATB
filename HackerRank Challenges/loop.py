"""
Task
The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print n**2.
"""
n = int(input("Enter the number = "))
if(1<=n<=20):
    for i in range(0,n):
        print(i**2)
else:
    print("Enter positive and valid number.")