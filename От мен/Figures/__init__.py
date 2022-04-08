from triangle import triangle
from square import square
from rectangle import rectangle
from rhombus import rhombus
from trapeze import  trapeze
print("Страни на триъгълник:")
a=int(input("a="))
b=int(input("b="))
triangle(a,b)
print("Страни на квадрат:")
a=int(input("a="))
square(a)
print("Страни на правоъгълник:")
a=int(input("a="))
b=int(input("b="))
rectangle(a,b)
print("Страни на ромб:")
a=int(input("a="))
h=int(input("h="))
rhombus(a,h)
print("Страни на трапец:")
a=int(input("a="))
b=int(input("b="))
h=int(input("h="))
trapeze(a,b,h)
