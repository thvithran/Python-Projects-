height = float(input("Enter the height in foot : "))
height_in_meter = height*12/39.37
weight=int(input("Enter weight in kg :"))
BMI =weight/pow(height_in_meter,2)
print("BMI :-",BMI)
if BMI > 25:
    print("Overweight")
elif BMI < 18:
    print("Underweight")
else:
    print("Fit")
