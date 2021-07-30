# Make a program that reads the width and height of a wall in meters, calculates its area and the amount of paint needed to paint it, knowing that each liter of paint paints an area of ​​2 square meters.

wall_height = float(input("Enter the height of the wall in meters: "))
wall_width = float(input("Enter the width of the wall in meters: "))
wall_area = wall_height * wall_width
ink_yeld = 2
necessary_paint = (wall_height * wall_width) / ink_yeld

print('yor wall has {}m² and you need {} liters of paint'.format(wall_area, necessary_paint))

