num = int(input("Enter No:"))
if num > 1:
    for i in range(2,num):
         if(num%i)==0:
             print("Not Prime Number")
             break
    else:
         print("It is Prime Number")
else:
     print("Not Prime Number")