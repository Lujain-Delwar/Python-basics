#Ans to qn 1
class Car:
    def __init__(self, brand, model, year):
        # Constructor initializes attributes
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self): #method to display car details
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


# Create object
car = Car("Toyota", "Corolla", 2026)

# Display details
car.display_info() #call method for output

#Ans to qn 2 part 1
class Animal:
    def eat(self):
        print("Animal is eating")

class Mammal(Animal):
    def walk(self):
        print("Mammal is walking")

class Dog(Mammal):
    def bark(self):
        print("Dog is barking")


# Create Dog object
dog = Dog()

dog.eat()
dog.walk()
dog.bark()

#Ans to qn 2 part 2
class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c


class AdvancedCalculator(Calculator):
    # Overriding the add method
    def add(self, a, b, c, d):
        return a + b + c + d


# Testing
cal = Calculator()
print("Calculator (2 numbers):", cal.add(5, 10))
print("Calculator (3 numbers):", cal.add(5, 10, 15))

adv_cal = AdvancedCalculator()
print("AdvancedCalculator (4 numbers):", adv_cal.add(5, 10, 15, 20))

#Ans to qn 3:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):
    def account_type(self):
        print("This is a Savings Account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a Current Account")

sa = SavingsAccount(1000)
ca = CurrentAccount(2000)

sa.deposit(500)
sa.withdraw(200)
print("Savings Balance:", sa.get_balance())

ca.deposit(1000)
ca.withdraw(500)
print("Current Balance:", ca.get_balance())

# Polymorphism
accounts = [sa, ca]

for account in accounts:
    account.account_type()