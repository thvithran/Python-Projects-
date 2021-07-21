#success
def getSum(n): # function name = getSum()   // argument = n
    sum = 0    # declare sum as 0
    for digit in str(n):  #for loop = variable name digit // declare n as string by using str() method
        sum += int(digit)
    return sum
n = 555
print(getSum(n))
