# ---OOP->Object oriented Programming is a programming paradigm that uses objects and classes
# to structure code. It allows for the creation of reusable and modular code by encapsulating
#  data and behavior into objects. In Python, OOP is implemented through the use of classes,
# which define the blueprint for creating objects.

#  example
# class --->Car
# object ---> BMW, Audi, Maruti, Tata, Honda

# class ClassName():
#     x=10

# p1=ClassName()
# print(p1.x)    


# class Person:
#     name="alash"
#     city="banaras"

# s1=Person()
# print(s1.name,s1.city) 


# this repetitive problem can be solved using __init__() method

# class Student():
#     def __init__():
#         print("Student object has got created!")

# s1=Student() # it will give error because __init__() method should have self parameter



# class Student():
#     def __init__(self):#self is a reference to the current instance of the class and is used to access variables that belong to the class.
#         print("Student object has got created!")

# s1=Student()




# class Student():
#     def __init__(self, name):
#         self.name=name

# s1=Student("Raj")
# print(s1.name)

# s2=Student("Ayushi")
# print(s2.name)



# class Person():
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city


# p1=Person("akash",23,'Banaras')
# print(p1.name,p1.age,p1.city)

# p2=Person('sahil',24,'khasipur')
# print(p2.name,p2.age,p2.city) 

# def display_profil(self):
#     print(self.name,self.age,self.city)

# s1=Person("akash",23,'Banaras') 
# s2=Person("sachin",25,'Banaras') 
# s3=Person("vikash",21,'delhi')    
# display_profil(s1)

# display_profil(s2)
# display_profil(s3)


# mini -case study
# A bank account class that allows users to create an account, deposit money, 
# withdraw money, and check their balance.

# class BankAccount():
#     def __init__(self,Account_holder,balance):
#         self.Account_holder=Account_holder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if self.balance < amount:
#             print("Insufficient Balance")
#         else:
#             self.balance-=amount

#     def show_balance(self):
#         print(self.balance)

# b1=BankAccount("akash",2500)
# print(b1.Account_holder)
# print(b1.balance)
# b1.deposit(5000)
# b1.deposit(1000)
# b1.withdraw(8500)
# b1.withdraw(2)
# b1.show_balance()

class Mobail:
    def __init__(self, brand):
        self.brand=brand

m=Mobail("Samsunng")
print(type(m))

print(hasattr(m,"brand"))
# it will be true
print(hasattr(m,"name"))
# it will be false



class Rectangle:
    def __init__(self, length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length *self.width    

r=Rectangle(4,5)
print(r.area())



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks >=40:
            print("Pass")
        else:
            print("Fail")   
s=Student("akash",55)
s.result()                 


class Student:
    def __init__(self, name):
        self.name=name

    def change_name(self,new_name):
        self.name=new_name
s=Student("akash")
s.change_name("vikash")
print(s.name)        


# #class variable and instance variable

class Student:
    college= "IIT Bombay"
    def __init__(self,name):
        self.name=name

s1=Student("Rahul")
s2=Student("akash")
print(s1.name,s1.college) 
print(s2.name,s2.college)    
s1.college="IIT Madras"   
print(s1.name,s1.college) 






# ----------Inheritance--------------------
       # parent class -->the class we are inherting from -->base class
       #child class--> the class that inherits frome another class-->derived class


class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def show_name(self):
        print(self.first_name,self.last_name)


p1=Person("akash",'patel')
p1.show_name()


class Student(Person):
    pass
s1=Student("rahul","kumar")
s1.show_name()



# questiom--
# create a parent class vehicles with __init__() method that takes make and model as parameters.
#  Create a child class Car that inherits from the Vehicle class and adds a new attribute num_doors.
#  Create an instance of the Car class and print its attributes.



class vehicles:
    def __init__(self,brand):
        self.brand=brand
    def display(self):
        print("Brand of the car is ",self.brand)
        
class Car(vehicles):
    pass

c1=Car("Suzuki")
c1.display()




# ---Polymorphism-----------

# same method name but different implementation in different classes
#polymorphism is the ability of an object to take on many forms. In Python, polymorphism is achieved through method overriding and operator overloading.

# example of method overriding
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows") 


# --HW--------------

class Car:
    def __init__(self,brand):
        self.brand=brand
car1=Car("BMW")
car2=car1
car2.brand='Audi' 
print(car1.brand)       


class Movie:
    def __init__(self,name):
        self.name=name


movie=Movie("Avatar")
print(hasattr(movie,'rating)'))




# ===
class Student:
    def greet(self):
        return "Welcome"

student=Student()  
message=student.greet()
print(message)  






 