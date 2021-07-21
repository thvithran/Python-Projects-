# Python program to get the Python version you are using
print("Excercise 1")
import sys
print(" Python Version")
print(sys.version)
print("Version info.")
print(sys.version_info)

print("-----------------------------------------------------------------------------------------------------------")
# Python program to display the current date and time.
print("Excercise 2")
import datetime
now = datetime.datetime.now()
print("Current date and time :")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print("------------------------------------------------------------------------------------------------------------")
# User Input First and Last name
print("Excercise 3")
firstname = input("Input your first name :")
lastname =  input("Input your last name :")
print("Hello"+firstname+" "+lastname)

print("------------------------------------------------------------------------------------------------------------")
# Program to generate a list and tuple comma-seperated numbers
print("Excercise 4")
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

print("-----------------------------------------------------------------------------------------------------------")
# Python program to accept a filename from the user and print the extension of that.
print("Excercise 5")
filename = input("Input the Filename :")
f_extns = filename.split(".")
print("The extenxion of the file is " +repr(f_extns[-1]))

# Print to calender
import calendar
y = int(input("Input the year :"))
m = int(input("Input the month :"))
print(calendar.month(y,m))



