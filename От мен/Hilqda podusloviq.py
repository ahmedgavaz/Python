class Conditions:
    def __init__(self,list1,list2,list3,name,rating,number):
        self.list1=list1
        self.list2=list2
        self.list3=list3
        self.name=name
        self.rating=rating
        self.number=number
    def adding(self):
        bol=True
        for i in self.list1:
            if self.name==i:
                bol=False
        if bol==True:
            self.list1.append(self.name)
            self.list2.append(self.rating)
            self.list3.append(self.number)
        else:
            print("This name is in the list")
        print(self.list1)
        print(self.list2)
        print(self.list3)  
    def remove(self):
        for i in range(len(self.list1)-1, 0, -1):
            if self.list2[i]<3:
                del self.list1[i]
                del self.list2[i]
                del self.list3[i]
        print(self.list1)
        print(self.list2)
        print(self.list3)        
    def middle(self):
        a=0
        for i in self.list2:
            a = a + i
        print("Sreden uspeh=", a/(len(self.list2)))
    def min_max(self):
        a=0
        b=0
        min=self.list2[0]
        max=self.list2[0]
        for i in range(1,len(self.list2),1):
            if min>self.list2[i]:
                min=self.list2[i]
                a=i
            if max<self.list2[i]:
                max=self.list2[i]
                b=i    
        print("Min:", min, "-",  self.list1[a])
        print("Max:", max, "-", self.list1[b])
    def copy(self):
        list4=[]
        for i in self.list1:
            if i[0]=="A":
                list4.append(i)
        print(list4)
    def equal(self):
        for i in range(len(self.list2)):
            for j in range(len(self.list2)-2):
                if self.list2[i]==self.list2[j+1]:
                    print("Name:", self.list1[i]," Rating:", self.list2[i]," Number:",self.list3[i]," ==>"," Name:", self.list1[j+1]," Rating:", self.list2[j+1]," Number:",self.list3[j+1])
    def num_rate(self):
        for i in range(len(self.list2)):
            if (self.list3[i] % 2==0) and (self.list2[i]==6):
                print("Name:", self.list1[i]," Rating:", self.list2[i]," Number:",self.list3[i])
    def move(self):
        list5=[]
        for i in range(len(self.list2)):
            if self.list2[i]==6:
                list5.append(self.list1[i])
        print(list5)        
    def num_min_rate(self):
        for i in range(len(self.list2)):
            if (self.list3[i] % 2==0) and (self.list2[i]<3):
                print("Name:", self.list1[i]," Rating:", self.list2[i]," Number:",self.list3[i])            

list1=['Ahmed Gavaz','Aksinia Fidosova', 'Aleksandar Avdzhiev',
       'Antonia Koleva', 'Dimitar Chavdarov', 'Dimitar Rabadzhiev',
       'Edis Madanski', 'Gergana Atanasova', 'Hristo Garkov',
       'Ines Damyanovska','Ivan Bashtenski', 'Ivan Kamenov', 'Ivan Stefanov',
       'Lorensia Davidkova','Marina Dimovska', 'Martin Genchev', 'Melis Ibisheva' ,
       'Mladen Chulev','Plamen Petrov', 'Radoslav Zdravkov', 'Sara Stanoevska',
       'Shteryu Atanasov',"Simona Mihova", 'Teona Denchevska', 'Tsvetan Vatovski',
       'Valensia Davidkova']            
list2=[4.76, 6.00, 5.32, 4.65, 3.64, 2.84, 3.43, 5.43, 3.68, 5.32, 4.24, 4.76,
       3.93, 3.55, 4.53, 5.87, 6.00, 5.13, 4.53, 3.93, 5.67, 3.54, 3.53, 3.25,
       5.23, 6.00]
list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
name=str(input("Name:"))
rating=float(input("Rating:"))
number=int(input("Number:"))
x= Conditions(list1,list2,list3,name,rating,number)
x.adding()
x.remove()
x.middle()
x.min_max()
x.copy()
x.equal()
x.num_rate()
x.move()
x.num_min_rate()
x.list3=[3,4,63,63,6,64,645,4564,64,6,46]
print(x.list3)
