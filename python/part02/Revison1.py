# -----------finding the frequency----------------

# text='banana'
# count={}
# for ch in text:
#     if ch not in count:
#         count[ch]=1
#     else:
#         count[ch]+=1
# print(count)
# print(count['a'])            

# # finding the second highest element
# marks=[85,90,75,95,80]
# highest=marks[0]
# for mark in marks:
#     if mark>highest:
#         highest=mark

# marks.remove(highest)
# print(max(marks))        

#------ print the subject whre the merks scored are atleast 85 and print in list

# student={
#     'marks':80,
#     'science':90,
#     'english':85
# }
# sub=[]

# for m in student:
#     if student[m]>=85:
#         sub.append(m)
# print(sub)    



# List → Mutable
# Set → Mutable
# Dictionary → Mutable
# Tuple → Immutable
# String → Immutable


# student=('akash',33,54)
# name,age =student
# # it will give error becuse only two elements are there in the tuple but 
# # we are trying to unpack three elements
 
# student=('akash',33,54)
# name,age ,mark,score =student
# it will give error becuse only three elements are there in the tuple but we are
#  trying to unpack four elements


# creating the empty set,list,dic,tuple

# l=[]
# t=()
# d={}
# s=set()



# problem 1---
# subject=['English',"Math",'Hindi','Computer','Science']
# marks=[]
# for i in subject:
#     print(i,'marks')
#     m=int(input())
#     marks.append(m)

# n=len(marks)
# average=sum(marks)/n
# print("average=",average)
# print("highest=",max(marks))
# print("lowest=",min(marks))

# if average>=90:
#     print('Grade=','A')
# elif average>=75:
#     print('Grade=','B')
# elif average >=60:
#     print('Grade=','C')
# else:
#     print('Grade=','D')    

# problem2
# word frequency counter

# words2="python is fun python is easy"
# words=words2.split(" ")
# count={}
# print(words)
# for i in words:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]+=1    

# print(count)




# problem 3
#take names seperate by space and remove  duplicate names  while preserving the first accurance


# name= 'Rahul Amit Rahul Neha Amit'
# name2=name.split()
# unique=[]
# for i in name2:
#     if i not in unique:
#         unique.append(i)
# print(unique)        

# # problem 3
# # take s string and count  number of vowel,consonant , digit , space
 
# s="Python3 is Fun"
# word=s.lower()
# vowel=0
# cons=0
# digit=0
# space=0
# for i in word:
#     if i in "aeiou":
#         vowel+=1
#     elif i in " ":
#         space+=1
#     elif i >='a' and i<='z':
#         cons+=1
#     else:
#         digit+=1

# print('vowel=',vowel)
# print('consonant=',cons)               
# print('digit=',digit) 
# print('space=',space) 


# # ----------or--------- using built in function

# s="Python3 is Fun"
# word=s.lower()
# vowel=0
# cons=0
# digit=0
# space=0
# for i in word:
#     if i in "aeiou":
#         vowel+=1
#     elif i.isalpha():
#         cons+=1
#     elif i.isdigit():
#         digit+=1        
#     elif i in " ":
#         space+=1
    

# print('vowel=',vowel)
# print('consonant=',cons)               
# print('digit=',digit) 
# print('space=',space) 



class BankAccount:
    def __init__(self,account_holder ,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount    

    def check_balance(self):
        print("Your available balance is = ",self.balance)


b1=BankAccount("vikas",2500)
print(b1.account_holder)
print(b1.balance)
b1.deposit(5000)
b1.withdraw(500)
b1.deposit(30000)
b1.check_balance()











