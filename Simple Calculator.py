# SIMPLE PYTHON CALCULATOR
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("SELECT OPERATION")
print("\n")
print("1. ADD")
print("2.Subtract")
print("3.Multiply")
print("4.Divide:")

while True:
# Take user input
  choice = input("Enter choice(1/2/3/4):")