import random
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
