#a program to print all the numbers between 1000 and 2000
# which are divisible by 7 but are not a multiple of 5.

for num in range (1000,2000):
    if num % 7 == 0 and num % 5 != 0:
        print(num)
