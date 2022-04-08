def func(b,c):
    for i in range(a):
        if b[i]>c:
            b[i]=0
    print(b)
a=int(input("Number of parameters in list:"))
b=[]
for i in range(a):
    c=int(input("Number=")) 
    b.append(c)
c=int(input("Number to compare="))             
func(b,c)
        
            
