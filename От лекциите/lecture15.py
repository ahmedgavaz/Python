class MyFirstClass:
    # class attribute /static variable
    i = 1234

    # constructor
    # def __init__(self):
    #     self.i = 22

    def __init__(self, i):
        self.i = i

    def f(self):  # self -> current instance
        return 'Hello Class!'

    def __str__(self):
        return "MyFirstClass(i="+str(MyFirstClass.i)+", self.i="+str(self.i)+")"

    def __repr__(self):
        return "MyFirstClass()"


print(MyFirstClass)
print(MyFirstClass.i)
print(MyFirstClass.f)
# print(MyFirstClass.f())

# x = MyFirstClass()  # constructor, x is object or class instance
x = MyFirstClass(121)
print(x.__str__())
print(x.i)
print(x.f())
print(x)
print(x.__repr__())
