# Make a program that reads any angle and displays the sine, cosine and tangent value of that angle on the screen.
import math
angle = float(input('Enter an angle: '))
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

print('sine: {:.2f}, cosine: {:.2f}, tangent: {:.2f}'. format(
    sine, cosine, tangent))
