# Program is to print the divisors of a number

num = int(input("Enter number :"))

for i in range(2,num):
    if num % i == 0:
        print(i)

