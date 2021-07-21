# CLASS 1
print("---- CLASS 1 : SHOE ----")
class Shoe():
    def __init__(self,brand,size,colour):
        self.shoebrand=brand
        self.shoesize=size
        self.shoecolour=colour
    def printname(self):
        print("Shoe brand =", self.shoebrand)
        print("Shoe size =", self.shoesize)
        print("Shoe colour = ", self.shoecolour)
        print("*****************************************")

shoe1=Shoe("Nike","10","black")
shoe2=Shoe("Adidas","11","white")
shoe3=Shoe("Puma","9","grey")
shoe4=Shoe("NB","12","blue")

shoe1.printname()
shoe2.printname()
shoe3.printname()
shoe4.printname()

#****************************************************************
# CLASS 2
print("--- CLASS 2: BOOK ---")
class Book:
    def __init__(self,name,year):
        self.book_name = name
        self.book_year = year

    def printname(self):
        print(self.book_name ,  self.book_year)

book1 = Book("Kamberamayanam","1789")
book2 = Book("Bible","1777")
book3 = Book ("al Quran ", "1878")


book1.printname()
book2.printname()
book3.printname()

#****************************************************************
print("***************************************************")
print("--- CLASS 3 : CAR ----")

class Car:
    def __init__(self,name,brand,colour):
        self.carname=name
        self.carbrand=brand
        self.carcolour=colour
    def printname(self):
        print("Car name : ",self.carname)
        print("Car brand :",self.carbrand)
        print("Car colour :",self.carcolour)
        print("***************************************")

car1=Car("Kancil","Perodua",1994)
car2=Car("Monster","Lambo",2010)
car3=Car("A1","Audi",2017)

car1.printname()
car2.printname()
car3.printname()

#***************************************************************
print("--- CLASS 4 : Phone ----")

class Phone():
    def __init__(self,name,brand,colour):
        self.phonename=name
        self.phonebrand=brand
        self.phonecolour=colour
    def printname(self):
        print(self.phonename,self.phonebrand,self.phonecolour)

phone1=Phone("I10","Xiomi","black")
phone2=Phone("S1","Vivo","lightblue")
phone3=Phone("10+","iPhone","white")

phone1.printname()
phone3.printname()
phone2.printname()
