class Library:
    def __init__(self, n, books, size, shelfid):
        self.nBooks = n
        self.books = books
        self.shelfid = shelfid
        self.__sizeShelf = size
        
    def getnBooks(self):
        return self.nBooks

    def setBooks(self, book):
        if self.nBooks < self._Library__sizeShelf:
            self.books.append(book)
            self.nBooks += 1
        else:
            print("Shelf is already full!\n")
            return
        
    def getBooks(self):
        return self.books
    

class Horror(Library):
    pass

class Adventure(Library):
    pass

class Cosmos(Library):
    pass


print("<-------------------Welcome to Iron Shelf Library-------------------->")
shelves = []
user = 'Y'
while user == 'Y':
    genre = str(input("What is the genre of this Shelf?: Horror, Adventure Cosmos:\n"))
    s = int(input("Enter the number of books this Shelf can contain:\n"))
    id = int(input("Declare the Shelf ID of this Shelf:\n"))
    if genre.lower() == "horror":
        shelf = Horror(0, [], s, id)
    elif genre.lower() == "adventure":
        shelf = Adventure(0, [], s, id)
    elif genre.lower() == "cosmos":
        shelf = Cosmos(0, [], s, id)
    else:
        print("Invalid Genre Choice!\n")
        continue
    
    shelves.append(shelf)
    
    while True:
        book = str(input("Enter the Book name: Enter done to exit\n"))
        if book.lower() == "done":
            break
        shelf.setBooks(book)
        
    user = input("Do you want to create another Shelf? (Y/N): ")
    
print("\nLibrary Overview:")
for shelf in shelves:
    print(f"Shelf ID: {shelf.shelfid}\nBooks: {shelf.getBooks()}\nNo.Books: {shelf.getnBooks()}")
    
print("<-------------Thank you for visiting Iron Shelf library-------------->")