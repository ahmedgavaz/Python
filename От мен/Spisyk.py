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

