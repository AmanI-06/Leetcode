"""There are two prerequisite conditions for Method overriding:

1. Inheritance should be present in the code, method overriding 
cannot be performed in the same class,and overriding can only
 be executed when a child class is derived through inheritance.

2. The child class should have the same name and the same number
 of parameters as the parent class."""

class Animal:
    def Walk(self):
        print('Hello, I am the parent class')

class Dog(Animal):
    def Walk(self):
        print('Hello, I am the child class')
        
print('The method Walk here is overridden in the code')

#Invoking Child class through object r

r = Dog()
r.Walk()

#Invoking Parent class through object r

r = Animal()
r.Walk()