# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, page, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.page = page
        self.price = price
        self.__secret = "This is a secret"
    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        self._discount = amount
# TODO: create some book instances
b1 = Book("War and Peace", "Tolstoy", 1225, 39)
b2 = Book("The Catcher in the Rye", "Salinger", 234, 15)

# TODO: print the price of book1
# print(b1.getprice())

# TODO: try setting the discount
print(b1.getprice())
b1.setdiscount(0.25)
print(b1.getprice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)