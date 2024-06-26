# Leap Year:
# leap year is divisible by 4,
# but not by 100 unless it is also divisible by 400
#
#Use an if-else statement to make  this determination

year = int(input("Enter a year: "))

(year % 4 == 0)
(year % 100 != 0)
(year % 400 == 0)

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")