tup1 = ()
n = int(input("Enter value"))
for i in range(1,n+1):
    tup1+=(i, )
    tup2 = sorted(tup1, reverse = True)
print(tup1)    
print(tup2)    
