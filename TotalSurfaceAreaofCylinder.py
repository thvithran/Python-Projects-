#import the constant pi from the math module
from math import pi

#cylinder height
h = float(input("h = "))

#cylinder base radius
r = float(input("r = "))

#a cylinder has two bases (top & bottom)
# area of each is Pi * R * R
circles = 2 * (pi * r ** 2)

# the area of the side surface of a cylinder
side = 2 * pi * r * h

#total surface area
area = circles + side

print("A =", round(area,2))