num=int(input("Enter number:"))
list1=[]
list2=[]
for i in range(1,num+1):
    list1.append(i)
dict={}
list2=list(list1)
list2.reverse()
for i in range(0,num):
    dict[list1[i]]=list2[i]  
print(dict)



