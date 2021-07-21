#taking user input
ch = input("Enter a character :")
dict=("a","e","i","o","u","A","E","I","O","U")

if ch in dict :
       print(ch,"is a vowel")
else:
       print(ch,"is a consonant")