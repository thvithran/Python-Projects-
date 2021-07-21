#Class (Self Excercise)
print("Class EXCERCISE 2")
print("*************************************** \n")

class myclass():
    def method1(self):
        print("Guru")
    def method2(self,someString):
        print("Python is"+someString)

c= myclass()
c.method1()
c.method2(" fun")

# Class Exercise 3
class Shark:
    def swim(self):
        print("The shark os swimming")
    def be_awesome(self):
        print("The shark is being awesome")

def main():
    sammy=Shark()
    sammy.swim()
    sammy.be_awesome()
