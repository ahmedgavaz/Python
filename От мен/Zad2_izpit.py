import json

class GSM_mobile_devices:
    def __init__(self, fnum, name, mark):
        self.quantity = quantity
        self.year = year
        self.manufacturer = manufacturer
        self.model = model

class Class:
    def __init__(self):
        self.group = []

    def append(self, gsm):
        self.group.append(gsm)

    def sort(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min][0] > self.group[j][0]:
                    min = j
            self.group[min][0], self.group[i][0] = self.group[i][0], self.group[min][0]

    def move(self):
        for i in range(len(self.group)):
            for j in range(i+1, len(self.group)):
                if self.group[0][i] == self.group[0][j]:
                    x=json.dumps(self.group[i][3])
    

