class Edureka():
    def __init__(self):
        self.course = "Python is a programming course"
        self.__tech = "python"
    def CourseName(self):
        return self.course + self.__tech

obj =Edureka()

print(obj.course)
print(obj._Edureka__tech)
print(obj.CourseName())
