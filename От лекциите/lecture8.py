class Shape:
    def __init__(self, number):
        self.number = number
        self.sides = [0 for x in range(number)]

    def inputSides(self):
        self.sides = [float(input('Enter side '+str(i+1)+' '))
                      for i in range(self.number)]

    def displaySides(self):
        print('(', end=' ')
        for i in range(self.number):
            print(self.sides[i], end=' ')
        print(')')

    def getPerimeter(self):
        return sum(self.sides)


class Triangle(Shape):

    def __init__(self):
        super().__init__(3)

    def getArea(self):
        p = self.getPerimeter()/2
        a, b, c = self.sides
        return (p*(p-a)*(p-b)*(p-c))**0.5  # math.sqrt


class RectangleOld(Shape):

    def __init__(self):
        Shape.__init__(self, 4)

    def getArea(self):
        a, b, c, d = self.sides
        return a*b


class Rectangle(Shape):

    def __init__(self):
        Shape.__init__(self, 2)

    def getArea(self):
        a, b = self.sides
        return a*b

# overriding -> virtual methods
    def displaySides(self):
        print('(', self.sides[0], ',', self.sides[1], ',',
              self.sides[0], ',', self.sides[1], ')')

    def getPerimeter(self):
        return super().getPerimeter()*2


t = Triangle()
#t.displaySides()
t.inputSides()
t.displaySides()
print(t.getPerimeter())
print(t.getArea())

# r = Rectangle()
# r.displaySides()
# r.inputSides()
# r.displaySides()
# print(r.getPerimeter())
# print(r.getArea())

# print(isinstance(t, Triangle))
# print(isinstance(t, Shape))
# print(isinstance(t, Rectangle))
# print(10*'=')
# print(isinstance(r, Triangle))
# print(isinstance(r, Shape))
# print(isinstance(r, Rectangle))
# print(isinstance(bool, int))
# print(isinstance(bool, float))
# x = 3
# print(isinstance(x, int))
# print(10*'=')
# print(issubclass(Rectangle, Shape))
# print(issubclass(bool, int))
# print(issubclass(bool, float))

# record=struct=>class without methods


class Employee:
    pass


john = Employee()
ivan = Employee()

john.name = 'John Dove'
john.age = 22
john.salary = 3000
john.job = 'developer'

print(john)
print(john.name, john.age, john.salary, john.job)

for x in [1, 2, 3]:
    print(x)

# iterator class


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


rev = Reverse([1, 2, 3, 4, 5, 6, 7, 8, 9])
for x in rev:
    print(x, end=' ')
print()

# generator


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for ch in reverse('I am Python Programmer'):
    print(ch, end=' ')
print()

xlist = [10, 20, 30]
ylist = [7, 5, 3]
print(sum(x*y for x, y in zip(xlist, ylist)))  # generator expression
# 10*7 + 20*5 + 30*3
