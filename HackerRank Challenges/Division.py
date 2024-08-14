"""
Task
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division, a // b.
The second line should contain the result of float division, a /b .
No rounding or formatting is necessary.
"""

a = int(input("Enter the 1st number = "))
b = int(input("Enter the 2nd number = "))


def division():
    print(f"The result of integer division is {a}//{b} = ", a // b)
    print(f"The result of float division is {a}/{b} = ", a / b)

division()