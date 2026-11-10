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



class Person():
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city


p1=Person("akash",23,'Banaras')
print(p1.name,p1.age,p1.city)

p2=Person('sahil',24,'khasipur')
print(p2.name,p2.age,p2.city) 

def display_profil(self):
    print(self.name,self.age,self.city)

s1=Person("akash",23,'Banaras') 
s2=Person("sachin",25,'Banaras') 
s3=Person("vikash",21,'delhi')    
display_profil(s1)

display_profil(s2)
display_profil(s3)


# mini -case study
# A bank account class that allows users to create an account, deposit money, 
# withdraw money, and check their balance.

class BankAccount():
    def __init__(self,Account_holder,balance):
        self.Account_holder=Account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance-=amount

    def show_balance(self):
        print(self.balance)

b1=BankAccount("akash",2500)
print(b1.Account_holder)
print(b1.balance)
b1.deposit(5000)
b1.deposit(1000)
b1.withdraw(8500)
b1.withdraw(2)
b1.show_balance()






