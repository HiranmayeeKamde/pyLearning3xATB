# Tringle Classiflier
# side1, side2, side3
#Equilateral => all sides are equeal
# Isosceles => any two sides are equal
# Scalene => all sides are different

side1 = int(input("Enter the side1: "))
side2 = int(input("Enter the side2: "))
side3 = int(input("Enter the side3: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
