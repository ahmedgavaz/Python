#mnojestva
s = set([1, 2, 3, 1])#list
print(s)
s2 = set("hello")#string
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
#remove(<element>)
#discard(<element>)
#pop( )
#clear( )
s1 = set([2, 4, 6])
s1.add(8)
print(s1)
s1.remove(2)
print(s1)
s1.pop()
print(s1)
