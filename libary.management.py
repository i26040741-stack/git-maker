class Book:
    def __init__(self,name,author,category):
        self.name = name
        self.author = author
        self.category = category
        self.available = True

    def display(self):
        print("-" * 20)
        print(f"Name: {self.name}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")
        print("=" * 20)

class libary:
    def __init__(self):
        self.books = []

    def add_books(self,name):
        self.books.append(name)

    def view_books(self):
        for number,item in enumerate(self.books,start=1):
            print(f"Number: {number}")
            item.display()
            if item.available:
                print("This book is available")
                print("="*20)
            else:
                print("out of the stock")
                print("="*20)

    def search_books(self,name):
        for item in self.books:
            if name.lower().strip() == item.name.lower().strip():
                if item.available:
                    print("This book is in the stock")
                else:
                    print("This book is borrowed")
                break
        else:
          print('This is out of the stock')

    def borrow_books(self,name):
        for item in self.books:
            if name.lower().strip() == item.name.lower().strip():
                if item.available:
                    print("This book is borrowed successfully!")
                    item.available = False
                    break
                else:
                    print("This book is borrowed")
                break
        else:
          print('This is out of the stock')

    def return_books(self,name):
        for item in self.books:
            if name.lower().strip() == item.name.lower().strip():
                if item.available:
                    print("This book is in the stock")
                else:
                    item.available = True
                    print(f"{name} is on the stock again")
                    break
                break
        else:
          print('This is out of the stock')

    def removed_books(self,name):
        for number,item in enumerate(self.books,start=1):
            print(f"Number: {number}")
            item.display()
        removed = self.books.pop(name -1)
        print(f"You just removed: {removed.name}")


def menu():
    print("=" * 25)
    print("1) Add Book")
    print("2) View Books")
    print("3) Search Book")
    print("4) Borrow Book")
    print("5) Return Book")
    print("6) Remove Book")
    print("7) Exit")
    print("=" * 25)

library = libary()

while True:
    menu()
    choice = int(input("Choose the option: "))
    if choice == 1:
        name = input("Type the name: ")
        author = input("Type the author: ")
        category = input("Type the category: ")
        new_book = Book(name,author,category)
        library.add_books(new_book)

    elif choice == 2:
        library.view_books()

        if not library.view_books():
            print("NO books installed yet!")
        
    elif choice == 3:
        name = input("search here: ")
        library.search_books(name)

    elif choice == 4:
        name = input("Type to borrow: ")
        library.borrow_books(name)

    elif choice == 5:
        name = input("Type to return: ")
        library.return_books(name)

    elif choice == 6:
        library.view_books()
        while True:
            try:
                name = int(input("Type name to remove: "))
            except ValueError:
              print('valid enter')
              continue
            if 1<= name <= len(library.books):
                library.removed_books(name)
                break
            else:
                print("Out of the range")
    elif choice == 7:
        print("Bye!!")
        break
    else:
        print("Valid enter!!")