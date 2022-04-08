def square(n):
    s=n*n
    print("S=", s)
def rectangle(a,b):
    s=a*b
    print("S=", s)
def triangle(a,b):
    s=(a*b)/2
    print("S=", s)
def rhombus(a,h):
    s=a*h
    print("S=", s)    
figure=input("Figure:")
if figure=="square":
    a=int(input("a="))
    square(a)      
elif figure=="rectangle":
    a=int(input("a="))
    b=int(input("b="))
    rectangle(a,b)
elif figure=="triangle":
    a=int(input("a="))
    b=int(input("b="))
    triangle(a,b) 
elif figure=="comparator" or figure=="rhombus":
    a=int(input("a="))
    h=int(input("h="))
    rhombus(a,h)
else:
    print("Error")    
