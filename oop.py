# Create a class called Student with:
# 1. A class variable university = "VU".
# 2. An __init__() constructor accepting name, age, and cgpa.
# 3. Store these as instance variables.
# 4. An instance method display() that prints student details.
# 5. A class method change_university() that updates the university name.
# 6. A static method is_passed(cgpa) that returns True if CGPA is at least 2.0, otherwise False.

class Student:
    university = "VU"

    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("cgpa: ", self.cgpa)

    @classmethod
    def change_university(cls, name):
        cls.university = name

    @staticmethod
    def is_passed(cgpa):
        return cgpa >= 2.0

s1 = Student("Azra", 21, 3.67)
s2 = Student("Rafia", 19, 3.1)

s1.display()
print(s2.university)
Student.change_university("Lahore uni")
print(s2.university)
print(s1.is_passed(1.9))


# Create a BankAccount class with:
# 1. A private attribute __balance, initialized through __init__().
# 2. A deposit(amount) method to add money.
# 3. A withdraw(amount) method that prevents withdrawal if the balance is insufficient.
# 4. A @property method called balance to read the balance.
# 5. A setter for balance that rejects negative values.
# Create an object and test deposits, withdrawals, and the property.

class Bank:

    def __init__(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        if(amount <= 0):
           print("Invalid amount")
        else:
          self.__balance += amount

    def withdraw(self, amount):
       if amount <= 0:
         print("Invalid amount")
       elif amount > self.__balance:
          print("Insufficient balance")
       else:
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if(amount < 0):
            print( "Invalid Amount")
        else:
            self.__balance = amount

b1 = Bank(3000)
print(b1.balance)
b1.deposit(2000)
print(b1.balance)
b1.withdraw(1000)
print(b1.balance)
b1.balance = -200
print(b1.balance)


# Create the following classes:
# 1. Person
# - Constructor: name, age.
# - Method: display() prints name and age.
# 2. Student(Person)
# - Add roll_no and cgpa.
# - Use super() to call the parent constructor.
# - Override display() to print all details.
# 3. Teacher(Person)
# - Add subject.
# - Use super() to call the parent constructor.
# - Override display() to print all details.
# Finally:
# - Create one Student and one Teacher.
# - Call display() on both objects.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("name: ", self.name)
        print("age: ", self.age)

class Student(Person):

       def __init__(self, name, age, cgpa, roll_no):
            super().__init__(name, age)
            self.cgpa = cgpa
            self.roll_no = roll_no
        
       def display(self):
            print(self.name)
            print(self.age)
            print(self.cgpa)
            print(self.roll_no)


class Teacher(Person):

     def __init__(self, name, age, subjects):
          super().__init__(name, age)
          self.subjects = subjects

     def display(self):
       print(self.name)
       print(self.age)
       print(self.subjects)
    

s1 = Student("student name", 21, 34, 3.67)
s1.display()

t1 = Teacher("teacher", 23, ["math", "chem"])
t1.display()

# Create an abstract class Shape:
# 1. Import ABC and abstractmethod from abc.
# 2. Create an abstract method area().
# 3. Create a child class Rectangle with length and width.
# 4. Implement area() in Rectangle.
# 5. Implement __str__() to return a readable description of the rectangle.
# Test it by creating a rectangle and printing:
# - Its area.
# - The rectangle object itself.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectange with length {self.length} and width {self.width}" 

r = Rectangle(10, 5)

print(r.area())
print(r)


# Requirements
# 1. Class: Book
# - Attributes: title, author, is_available.
# - Method: display().
# 2. Class: Library
# - Private attribute: __books (a list of books).
# - Method: add_book(book) — adds a book.
# - Method: show_books() — displays all books.
# - Method: borrow_book(title) — borrows a book if available.
# - Method: return_book(title) — returns a borrowed book.
# 3. Demonstrate:
# - Create at least three books.
# - Add them to the library.
# - Display all books.
# - Borrow one book.
# - Try borrowing the same book again.
# - Return the book.

class Book:

    def __init__(self, title, author, is_avaiable):
        self.title = title
        self.author = author
        self.is_available = is_avaiable

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:

    def __init__(self, books):
        self.__books = books

    def add_book(self, book):
        self.__books.append(book)

    def show_book(self):
        for book in self.__books:
            print(book)

    def borrow_book(self, title):
     for book in self.__books:
        if book.title == title:
            if book.is_available:
                book.is_available = False
                print("Book borrowed successfully")
            else:
                print("Book already borrowed")
            return

     print("Book not found")

    def return_book(self, title):
     for book in self.__books:
        if book.title == title:
            if not book.is_available:
                book.is_available = True
                print("Book returned successfully")
            else:
                print("Book was not borrowed")
            return

     print("Book not found")

    
b1 = Book("Python", "Eric Matthes", True)
b2 = Book("Clean Code", "Robert Martin", True)
b3 = Book("Atomic Habits", "James Clear", True)

print(b1)

lib = Library([b1, b2, b3])

# 1. Show all books
print("\nAll Books:")
lib.show_book()

# 2. Borrow Python
print("\nBorrow Python:")
lib.borrow_book("Python")

# 3. Try borrowing Python again
print("\nBorrow Python Again:")
lib.borrow_book("Python")

# 4. Borrow a book that doesn't exist
print("\nBorrow Java:")
lib.borrow_book("Java")

# 5. Return Python
print("\nReturn Python:")
lib.return_book("Python")

# 6. Return Python again
print("\nReturn Python Again:")
lib.return_book("Python")

# 7. Show books again
print("\nFinal Book List:")
lib.show_book()