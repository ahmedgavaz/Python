k=(7,5,3)
print(k)

#tuple()-syzdavane na prazen kortej

#preobrazuvane na spisyk v kurtej:
tup=tuple([10,20,30,])
print(tup)

#preobrazuvane na niz v kurtej:
tup1=tuple("python")
print(tup1)
tup

k=(7, 5, 3, 6, 1)
print(k[0])#dostyp do element po index
print(k[2:3])#sechenie
print(7 in k)#proverka za nalichie na element
print(k*3)#povtorenie
tup =k + (2, 4)#konkatenaciq
print(tup)

tup = (7, 5, 3, 6, 1)
print(tup.index(1))#4
print(tup.count(5))#1

#obhojdane na elementite na kortejite
for i in tup:
    print(i)
