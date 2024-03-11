#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self, library):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' by {self.author} has been borrowed.")
        else:
            print(f"Book '{self.title}' by {self.author} is not avialable in libarary rn.")
      
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"Book '{self.title}' by {self.author} is already available.")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_available_books(self):
        available_books = [book.title for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book_title in available_books:
                print("- ", book_title)
        else:
            print("No books available in the library.")

# Create instances of Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("Harry Potter", "JK Rowling")
book3 = Book("Wimpy Kid", "Jeff Kinney")

# Create instance of Library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

def optionss():
    while True:
        action = input("Do you want to view available books, borrow or return books? (view/borrow/return/exit): ")
        if action.lower() == "view":
            library.display_available_books()
        elif action.lower() == "borrow":
            book_title = input("Enter the title of the book you want to borrow: ")
            book_found = False
            for book in library.books:
                if book.title.lower() == book_title.lower():
                    book.borrow(library)
                    book_found = True
                    break
            if not book_found:
                print(f"Book '{book_title}' is not available in the library.")
        elif action.lower() == "return":
            book_title = input("Enter the title of the book you want to return: ")
            for book in library.books:
                if book.title.lower() == book_title.lower():
                    book.return_book()
                    break
            else:
                print(f"Book '{book_title}' is not available in the library.")
        elif action.lower() == "exit":
            print("Thank you for using the library. Goodbye!")
            break
        else:
            print("Invalid action. Please enter view, borrow, or return.")

optionss()


# In[ ]:


class Asset:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def value(self):
        return self.quantity * self.price


class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def remove_asset(self, asset_name):
        for asset in self.assets:
            if asset.name == asset_name:
                self.assets.remove(asset)
                return
        print(f"Asset '{asset_name}' not found in the portfolio.")

    def total_value(self):
        total = sum(asset.value() for asset in self.assets)
        return total

    def display_assets(self):
        if not self.assets:
            print("Portfolio is empty.")
        else:
            print("Assets in the portfolio:")
            for asset in self.assets:
                print(f"Name: {asset.name}, Quantity: {asset.quantity}, Price: {asset.price}, Total Value: {asset.value()}")


# Example usage
stock1 = Asset("AAPL", 10, 150)  # Stock asset
bond1 = Asset("US Bonds", 5, 1000)  # Bond asset
cash = Asset("Cash", 2000, 1)  # Cash asset

portfolio = Portfolio()
portfolio.add_asset(stock1)
portfolio.add_asset(bond1)
portfolio.add_asset(cash)

portfolio.display_assets()

print("Total portfolio value:", portfolio.total_value())

portfolio.remove_asset("AAPL")

portfolio.display_assets()

print("Total portfolio value:", portfolio.total_value())

