class MyGroup():
    def __init__(self,list1,list2,list3,list4,list5,list6,a):
        self.list1=list1
        self.list2=list2
        self.list3=list3
        self.list4=list4
        self.list5=list5
        self.list6=list6
        self.a=a
    def move(self):
        s=[]
        for i in range(len(self.list1)):
            if self.list2[i]>=5.5:
                s.append(self.list1[i])
        print(s)        
    def move1(self):
        for i in range(len(self.list1)):
            for j in range(len(self.list1)):
                if self.list2[i]==self.list2[j]:
                    if i!=j:
                        if j>i:
                            print(self.list1[i], self.list2[i], self.list3[i],self.list1[j],self.list2[j],self.list3[j])
    def move2(self):
        for i in range(len(self.list1)):
            if self.list3[i]%2>0:
                if self.list2[i]<3:
                    print(self.list1[i], self.list2[i], self.list3[i])
    def move3(self):
        for i in range(len(self.list1)):
            self.list1[i]=self.list1[i].upper()
            print(self.list1[i])
    def prihod(self):
        bol=False
        x=0
        for i in range(len(self.list4)):
            if self.a==self.list4[i]:
                self.list5[i]=self.list5[i]*0.9
                bol=True
        if bol==False:
            print("0000")
            print("Zaredi produkta")
        for j in range(len(self.list4)):
            x=x+self.list5[j]
        print("Sredno aritmetichno=",x/len(self.list4))
list1=['Ahmed Gavaz','Aksinia Fidosova', 'Aleksandar Avdzhiev',
       'Antonia Koleva', 'Dimitar Chavdarov', 'Dimitar Rabadzhiev',
       'Edis Madanski', 'Gergana Atanasova', 'Hristo Garkov',
       'Ines Damyanovska','Ivan Bashtenski', 'Ivan Kamenov', 'Ivan Stefanov',
       'Lorensia Davidkova','Marina Dimovska', 'Martin Genchev', 'Melis Ibisheva' ,
       'Mladen Chulev','Plamen Petrov', 'Radoslav Zdravkov', 'Sara Stanoevska',
       'Shteryu Atanasov',"Simona Mihova", 'Teona Denchevska', 'Tsvetan Vatovski',
       'Valensia Davidkova']            
list2=[4.76, 6.00, 5.32, 4.65, 3.64, 2.84, 3.43, 5.43, 3.68, 5.32, 4.24, 4.67,
       3.93, 3.55, 4.53, 5.87, 6.00, 5.13, 4.53, 3.93, 5.67, 3.54, 3.53, 3.25,
       5.23, 6.00]
list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
list4=[100,101,102,103,104,105,106,107,108,109,110]
list5=[5.64,3.64,8.48,12.43,15.34,8.66,2.14,4.67,13.43,24.32,15.32]
list6=[23,42,34,12,21,42,21,23,12,63,44]
a=int(input("Write a code:"))
w=MyGroup(list1,list2,list3,list4,list5,list6,a)
w.move()
w.move1()
w.move2()
w.move3()
w.prihod()

