#python swap program
x = input("Enter the value x :")
y = input("Enter the value of y :")

#create a temporary variable and swap the values
temp = x
x = y
y = temp

print("The value of x after swapping : {}".format(x))
print("The value of y after swapping : {}".format(y))