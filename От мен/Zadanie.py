class MyGroup():
    def __init__(self,list1,list2,name,grade):
        self.list1=list1
        self.list2=list2
        self.name=name
        self.grade=grade
    def adding(self):
        bol=True
        for i in range(len(self.list1)-1):
            if self.name==self.list1[i]:
                bol=False
        if bol==True:
            self.list2.append(self.grade)
            self.list1.append(self.name)
    def remove(self):
        a=[]
        for j in range(len(self.list2)-1):
            if self.list2[j]<3:
                a.append(j)
        t=len(a)-1
        while t>-1:
            self.list1.pop(a[t])        
            self.list2.pop(a[t])
            t=t-1
    def uspeh(self):
        a=0
        for d in range(len(self.list1)):
            a=a+self.list2[d]
        print(a/len(self.list2))    
    def show(self):
        print(self.list1)
        print(self.list2)
def recording(f,list):
    f=open("studeni.txt", "a+")
    for i in list:
        f.writelines(str(i) + " ")
    file.close()
    
list1=['Ahmed Gavaz','Aksinia Fidosova', 'Aleksandar Avdzhiev',
       'Antonia Koleva', 'Dimitar Chavdarov', 'Dimitar Rabadzhiev',
       'Edis Madanski', 'Gergana Atanasova', 'Hrisot Garkov',
       'Ines Damyanovska','Ivan Bashtenski', 'Ivan Kamenov', 'Ivan Stefanov',
       'Lorensia Davidkova','Marina Dimovska', 'Martin Genchev', 'Melis Ibisheva' ,
       'Mladen Chulev','Plamen Petrov', 'Radoslav Zdravkov', 'Sara Stanoevska',
       'Shteryu Atanasov',"Simona Mihova", 'Teona Denchevska', 'Tsvetan Vatovski',
       'Valensia Davidkova']            
list2=[4.76, 6.00, 5.32, 4.65, 3.64, 2.84, 3.43, 5.43, 3.68, 5.32, 4.24, 4.67,
       3.53, 3.55, 4.53, 5.87, 6.00, 5.13, 2.53, 3.53, 5.67, 3.54, 3.53, 3.25,
       5.23, 6.00]
a=input("Write a name:")
b=float(input("Write a grade:"))
file=open("studeni.txt", "a+")
recording(file,list1)
recording(file,list2)
x=MyGroup(list1,list2,a,b)
x.adding()
x.remove()
x.uspeh()
x.show()
