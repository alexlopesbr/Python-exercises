# show the triangle type

# EQUILATERAL: all sides equal
# ISOSCELES: two sides equal
# SCALENE: all sides different

side_1 = float(input('Enter the first side: '))
side_2 = float(input('Enter the second side: '))
side_3 = float(input('Enter the third side: '))

if side_1 < side_2 + side_3 and side_2 < side_1 + side_3 and side_3 < side_1 + side_2:
    print('The triangle is valid.')

    if side_1 == side_2 == side_2 == side_3:
        print('Equilateral')
    elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
        print('Isosceles')
    elif side_1 != side_2 != side_3 != side_1:
        print('Scalene')
    else:
        print('unidentified triangle.')
else:
    print('The triangle is invalid.')
