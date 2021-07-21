# The math module containing various math functions is imported
import math

#the input() function return a string
AB = input("Length of the first leg :")
AC = input("Length of the second leg:")

#strings are converted to real numbers
AB = float(AB)
AC = float(AC)

# Find the hypotenuse by the Pythagorean theorem :
#
#    "The sum of the squares of the legs is equal to the square of the hypotenuse"
#
# The sqrt() function of the math module extract a square root.
# The operator  ** raises a number to a power.

BC= math.sqrt(AB ** 2 + AC ** 2)

#The area of right triangle is equal to half the area of the corresponding rectangle.

S = (AB * AC)/2

#Perimeter is the sum of all sides
P = AB + AC + BC

print("Area of triangle : %.2f" % S)
print("Perimeter of the triangle : %.2f" % P)
