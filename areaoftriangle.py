# Program to calculate  the area of triangle
#-----------------------------------------------------------
# Mathematic Formula
# Area of triangle = (s*s(s-a)*(s-b)*(s-c)) -1/2
#------------------------------------------------------------

#three sides of triangle is a,b,c
a=float(input("Enter first side :"))
b=float(input("Enter second side:"))
c=float(input("Enter third side :"))

#calculate the semi perimeter
s=(a+b+c)/2

#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of triangle is %0.2f"%area)