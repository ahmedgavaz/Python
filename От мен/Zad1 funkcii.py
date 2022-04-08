def palin(a,b):
    for i in range(len(a)//2):
        if a[i]!=a[len(a)-1-i]:
            b=0
    print(b)
a=input("Number=")
b=1
palin(a,b)
    
