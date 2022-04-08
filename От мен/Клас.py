#syzdavane na klas s ime i svoistvo:
class MyFirstClass:
    x=5

#syzdavane na obekt, baziran na syzdaden klas:
MyFirstObject= MyFirstClass()

#dostypvane elemntite na klasa:
print(MyFirstObject.x)

#funkciqta konstructor __init__()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
MyPerson=Person("Ivan",35)
print(MyPerson.name)
print(MyPerson.age)

#Metodi:

class Person:
     def __init__(self,name,age):
        self.name=name
        self.age=age
     def greetings(self):
         print("Hello, my name is "+self.name)
MyPerson=Person("Ivan",35)
MyPerson.greetings()

#parametyr self

#promqna na stoinostite na svoistvata na obekti:
MyPerson.age=40

#iztrivane svoistvata na obekti s del:
del MyPerson.age

#iztrivane na celi obekti s del:
del MyPerson

#definirane na klas bez sydyrjanie (pass)
class Person:
    pass

#nasledqvane:


         
            
