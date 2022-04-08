def Add(a,b):
    print(a+b)
def Subtration(a,b):
    print(a-b)
def Multiplication(a,b):
    print(a*b)
def Division(a,b):
    print(a/b)  
operation=input("Operation:")
if operation=="+" or operation=="-" or operation=="*" or operation=="/":
    a=int(input("Number 1="))
    b=int(input("Number 2="))
    if operation=="+":
        Add(a,b)     
    elif operation=="-":
        Subtration(a,b)
    elif operation=="*":
        Multiplication(a,b)
    else:
         Division(a,b)
