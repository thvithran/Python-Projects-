print("Exercise 1")
# Single Inheritnace
class Grandpa():
     print("I'm a grandpa")

class Father(Grandpa):
     print("I'm a father")

class Son(Father):
     print("I'm a son")

Thvi = Son()

#*******************************************************
print("\n")
print("Excercise 2")

class App:
    def start(self):
       print('starting')

class Android(App):
    def getVersion(self):
       print('Android version')

app = Android()
app.start()
app.getVersion()