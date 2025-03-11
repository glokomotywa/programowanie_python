class Person:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} i mam {self.wiek} lat.")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Niewystarczające środki!")
        else:
            self.balance -= amount

class Student:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = []

    def add_grade(self, name, grade):
        if name in self.students:
            self.students[name].append(grade)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

class User:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if self.users.get(username) == password:
            return True
        return False
