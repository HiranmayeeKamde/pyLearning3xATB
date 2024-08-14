# * args -> any no of arguments
print("Eknath","Varsha", "Gaurav")

def sum(a = 1,b = 1,c = 1):
    return a+b+c
result1 = sum(10, 20, 30)
result2 = sum()
result3 =sum(a=9)
result4 =sum(9,9)
result5 =sum( a=9, c=11, b= 9)
print(result1, result2, result3, result4, result5)