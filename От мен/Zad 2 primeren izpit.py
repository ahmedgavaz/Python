class Travel:
    def __init__(self,ID,Destination,Flight,Price):
        self.ID=ID
        self.Destination=Destination
        self.Flight=Flight
        self.Price=Price
    def Reduce(self):
        if self.Price>200:
            self.Price=round(self.Price*0.9,1)
    def Print(self):
        print("ID:",self.ID)
        print("Destination:",self.Destination)
        print("Flight:",self.Flight)
        print("Price:",self.Price)
        print(" ")
x=Travel(143350,"Amsterdam",421,141)
x.Reduce()
x.Print()
x=Travel(143242,"Madrid",461,286)
x.Reduce()
x.Print()
x=Travel(142535,"New York",434,441)
x.Reduce()
x.Print()
x=Travel(145353,"Istanbul",442,112)
x.Reduce()
x.Print()
