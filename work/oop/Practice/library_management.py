class library:
    books = []
    bookdict = {}

    def display(self):
        print()
        for i in self.books:
            print(i, end=", ")

    def addbook(self ,bookname):
        self.books.append(bookname)

    def lendbook(self, personname, bookname):
        self.books.remove(bookname)
        self.bookdict[bookname] = personname

    def lendlist(self):
        print()
        print(self.bookdict)

    def returnbook(self,bookname):
        self.books.append(bookname)
        self.bookdict.pop(bookname)

lib = library()
lib.addbook("kite")
lib.addbook("sneaker")
lib.addbook("childhood")
lib.addbook("uncle han")
lib.addbook("legends")

lib.display()
lib.lendbook("prithvi", "kite")
lib.display()
lib.lendlist()
lib.returnbook("kite")
lib.display()
lib.lendlist()


