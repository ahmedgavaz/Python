class Person:
    def __init__(self, name, family, age, nationality):
        self.name=name
        self.family=family
        self.age=age
        self.nationality=nationality
    def show(self):
        print("Hello, my name is " + self.name + " " + self.family + 
              " and I am " + " " + self.nationality)
class Student(Person):
    def __init__(self,university,year_of_study):
        self.university=university
        self.year_of_study=year_of_study
    def show(self):
        print("I study at " + self.university + " from "
              + self.year_of_study + " year!")
class Lecturer(Person):
    def __init__(self,university,experience):
        self.university=university
        self.experience=experience
    def show(self):
        print("Mr Ivan Ivanov is lecturer at " + self.university +
             " and has " + self.experience + " years of experience!")        
MyPerson=Person("Ahmed", "Gavaz", 19, "Bulgarian!!!")
MyPerson.show()
MyPerson=Student("Technical university of Sofia", "2021")
MyPerson.show()
MyPerson=Lecturer("Technical university of Sofia", "40")
MyPerson.show()

