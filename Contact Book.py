names = []
phone_numbers = []
num = 10    # can adjust number of cantacts that we can add in contact list


for i in range(num):
    name=input("Name :")
    phone_number=int(input("Phone Number :"))

    names.append(name)
    phone_numbers.append(phone_number)

print(" \n Name  \t\t\t Phone Number \n")

for i in range (num):
    print("{}  \t \t \t {}".format(names[i],phone_numbers[i]))

search_term = input(" \n Enter search term :")

print("Search result :")

if search_term in names:
    index = names.index(search_term)
    phone_number =phone_numbers[index]
    print("Name:{},Phone Number:{}".format (search_term,phone_number))
else:
    print("Name Not Found")