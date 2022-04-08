class Sentence:
    def __init__(self, sent):
        self.sent = sent
    def Change(self):
        a=[]
        b=""
        br=0
        for i in range(len(self.sent)):
            if self.sent[i]!=" ":
                b+=self.sent[i]
            else:
                a.append(b)
                b=""
                br=br+1
        a.append(b)        
        a.reverse()
        for i in range(br+1):
            print(a[i], end=" ")
x=input("Wirte sentence:")
y=Sentence(x)
y.Change()

                       
