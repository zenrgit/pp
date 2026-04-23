# Single level inheritance example
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def display(self):
        print("This is the Child class.")

c=Child()
c.show()    # Inherited method from Parent class
c.display() # Method of Child class


# Multilevel inheritance example
class Grandparent:
    def greet(self):
        print("Hello from the Grandparent class.")

class Parent2(Grandparent):
    def show(self):
        print("This is the Parent class.")

class Child2(Parent2):
    def display(self):
        print("This is the Child class.")

x=Child2()
x.greet()   # Inherited method from Grandparent class
x.show()    # Inherited method from Parent class
x.display() # Method of Child class
