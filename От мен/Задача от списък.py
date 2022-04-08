import random
a=[random.randint(10,20) for i in range(16)]
for i in range(0, 22, 3):
    a.insert(i+2, a[i]+a[i+1])
print(a)
#a.insert(2, a[0]+a[1])
#a.insert(5, a[3]+a[4])
#a.insert(8, a[6]+a[7])

