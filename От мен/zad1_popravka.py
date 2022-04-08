n = int(input("Number n="))
k = int(input("Number k="))
s=[]
t=[]
pr=1

for i in range(n-1):
    a = int(input("a="))
    if (a > k):
        s.append(a)
    if (a <= k and a > 0):
        t.append(a)
min = s[0]
ind = 0
for j in range(len(s)):
    if (j % 2 ==1):
        pr = pr * s[j]
    if (min > s[j]):
        min = s[j]
        ind = j
min1 = t[0]
max = t[0]
for v in range(len(t)):
    if (min1 > t[v]):
        min1 = t[v]
    if (max < t[v]):
        max = t[v]
print(s)
print("Umnojenie=", pr)
print("Index min=",ind)
print(t)
print("Min=",min1)
print("Max=",max)
print("Razlika=",max - min1)
