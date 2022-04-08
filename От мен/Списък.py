import random
s=[1,3,5,7,]
print(s[1])

s[1]=11
print(s)

s=list()
s1=list["Python"]
print(s1)

s=["P","Y","T","H","O","N",3]
print(s)

s=[]
s.append(5)
s.append(10)
s.append(20)
print(s)

s=[2,4,6,8]
s[0]=7
print(s[0])

#[<nachalo>:<krai>:<stypka>]

s=[1,2,3,4,5,6]
print(s[::-1])#извеждане на елементите в обратен ред
print(s[:-1])#принтиране без последния елемент
print(s[1:])#принтиране без първия елемент
print(s[0:2])#принтиране на първите два елемента
print(s[-1:])#принтиране на последния елемент


s=[1,2,3,4,5,6]
s1=[9,8]
s2=s+s1
print(s2)

s=[[1,2,3,4,5], ["a", "b", "c"], [10,20]]
print(s[0][3])
print(s[2][0])

s=[1,2,3,4,5,6]
for i in s:
    print(i, end="")

s=[1,2,3,4,5,6]
for i in range (len(s)):
    print(s[i], end="")

s=[2,4,6,8]
print(4 in s)#True
print(9 in s)#False

s=[2,4,6,8,2]
print(s.count(2))#2
#print(s.index(3))#ValueError
print(min(s))#2
print(max(s))#8

#append()-dobavqne na kraq
#(+=)-dobavqne na kraq
#insert(<index>,  <element>)-dobavqne v posochena poziciq
#pop()-iztrivane na element s posochen index
#remove()-premahvame na element s opredelena stoinost v skobite
#del-iztrivane na element s posochen index

s=[2,4,6,8,2]
s.append(22)
print(s)

s+=[44,88]
print(s)

s.insert(0,90)
print(s)

s.pop(0)
print(s)

s.remove(2)
print(s)

del s[4]
print(s)

#shuffle()-za razbyrkvane na elemnetite na spisyk

s=[2,4,6,8,2]
random.shuffle(s)
print(s)
print(random.choice(s))
s.reverse()
print(s)

#reverse()-obryshta reda

#sort()-sortirane
#sort(<key=None>,<reverse=False>)
#reverse=True(ako iskame da obyrnem reda)
s=[45,10,55,5,35]
s.sort()
print(s)
s.sort(reverse=True)
print(s)

#key=str.lower-za stringove

s1=["s","T","a","E","f"]
s1.sort(key=str.lower)
s1.sort()
print(s1)

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

#syzdavane na rechnik
d=dict()
d1=dict(name='ivan', last_name='petrov')
d3=dict([ ('name', 'polina'), ('l_name', 'koleva')])
print(d3)
print(d1)

#zapylvane na rechnik element po element
d= { }
d['name'] = 'petyr'
d['last_name'] = 'kolev'
d = {'name':'ivan', 'last_name': 'ivanov'}
print(d)

#operacii
d = {'name': 'ivan', 'last_name': 'ivanov'}
d['name']
#print(d[d['fname']) - greshka

#proverka za nalichie na kliuch chrez operator in
b = 'fname' in d
print(b) #false

#opredelqne na broq na kliuchovete v rechnika
len(d)
print(len(d))#2

#dobavqne na elementi v rechnika
d['s_name'] = 'petrov'
print(d)

#premahvane na elemnt ot rechnik - izpolzva se del
del d['s_name']
print(d)

#metodi keys() i value()
keys = list(d.keys())
keys.sort()
for key in keys:
    print("{0} => {1} ".format(key, d[key]), end=' ')

#mnojestva
s = set([1, 2, 3, 1])#list
print(s)
s2 = set("hello")#string

#operacii pri mnojestva
#obhojdane na mnojestvo
s2 = set("hello")
for i in s2:
    print(i, end=' ') # lheo

#funkciq len()
print(len(s2))#4

#obedinenie na mnojestva
s = set([1, 2, 3])
s1 = set([4, 2, 6])
s3 = s | s1
print(s3)

#razlika na mnojestva
s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])
s2 = s - s1
print(s2)
s3= s1-s
print(s3)

#presichane na mnojestva - obshtite elementi
s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])
s4 = s &s1
print(s4)

#Operaciq izkliuchvashto ili ^
s = set([1, 2, 3, 4])
s1 = set([2, 4, 6])
s5 = s ^ s1
print(s5)#{1, 3, 6} izvejda elementite koito ne sa obshti

3 in s #True

#metodi na mnojestvata
#add(<element>)
#remove(<eement>)
#discard(<element>)
#pop( )
#clear( )
s1 = set([2, 4, 6])
s1.add(8)
print(s1)
s1.remove(2)
print(s1)
#s1.remove(2)-Error
