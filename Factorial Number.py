def fact(n):    #factorial function with name fact // argument is n
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fac = 1
        while(n > 1):
            fac = fac * n
            n = n-1
        return fac
num = 6
print("Factorial :",fact(num))
