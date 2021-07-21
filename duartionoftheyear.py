#import the constant  pi from the math module
from math import pi

r = input("Radius of orbit (million km) :")
v = input("Orbital speed (km/s):")

#string are converted to float numbers
r = float(r)
v = float(v)

#translate millions of km into just kilometres
r = r * 1000000

#Year ,expressed in seconds. The length of circumstance is being found (2*Pi*R), that is the orbit and divided by the speed
year = 2 * pi * r /v

#To translate seconds into days,
# You need to divide by 60 and get the minutes, then divide by 60 and get the hours, then divide by 24 and get the days
year = year/ (60*  60 *24)

#output command
print(round(year))
