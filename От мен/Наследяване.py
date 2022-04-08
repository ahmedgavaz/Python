#Nasledqvane:

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)

MyPerson=Person("Ivan","Petrov")
MyPerson.printname()

class Student1(Person):
    pass

class Student(Person):
    def __init___(self,fname,,lname):
        Person.__init__(self,fname,lname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(self,fname,lname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(self,fname,lname)
    self.graduationyear=year    

            
