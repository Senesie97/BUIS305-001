import math

for count in range(0, 11):
    print(count, end = " ")
for count in range(1, 11):
    print(count, end = " ")
for count in range(1, 11, 2):
        print(count)
radius = float(input('Enter Radius'))
if radius > 0:
    print('Valid Input')
    area = 3.14 * radius * radius
    print(area)
else:
    print('Invalid Input')
length = float(input('Enter length'))
breadth = float(input('Enter breadth'))
if length and breadth > 0:
        print('Valid Input')
        area1 = length * breadth
        print(area1)
else:
    print('input parameters are not greater than 0 and you can’t compute area of the requested polygon')