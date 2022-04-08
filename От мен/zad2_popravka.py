class Book:
    def __init__(self,book_name,book_code,book_price,book_year,book_author):
        self.name = book_name
        self.code = book_code
        self.price = book_price
        self.year = book_year
        self.author = book_author

class Class:
    def __init__(self, search):
        self.group = []
        self.search

    def append(self, book):
        self.group.append(book)

    def sort(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min][0] > self.group[j][0]:
                    min = j
            self.group[min][0], self.group[i][0] = self.group[i][0], self.group[min][0]

    def author(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min][4]== self.group[j][4]:
                    print(self.group[min][4]+ " ->" + self.group[j][4])

    def search_book(self):
        bol = True
        for i in range(len(self.group)):
            f self.group[i][1] == self.search:
                bol = False
                print(self.year)
        if (bol == True):
            print("The book is not found.")
            
                    
