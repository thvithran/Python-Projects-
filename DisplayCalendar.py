# import calendar ---> calendar header file

import calendar

# Enter the month and year

yy = int(input("Enter the year :"))
mm = int(input("Enter the month :"))

# display the calendar
print(calendar.month(yy,mm))
