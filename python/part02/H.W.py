# problem statment--
# a password is valid if contains
# -minimum 8 character
# atleast one lowercase  letter 
# atleast one upperrcase  letter 
# atlest one digit
# display starong password and weak password

# password=input("Enter the password=")
# n=len(password)
# upper=False
# lower=False
# digit=False
# for c in password:
#     if c.islower():
#         lower=True
#     elif c.isupper():
#         upper=True
#     elif c.isdigit():
#         digit=True

# if n>=8 and upper and lower and digit:
#     print("Strong Password")
# else:
#     if n<8:
#         print("passwor must be 8 character")
#     else:
#         if upper!=True:
#             print("Weak Password")
#             print("Please contain the uppercase  letter in your password ")
#         elif lower!=True:
#             print("Weak password")
#             print("Please contain the lowercase  letter in your password")
#         elif digit!=True:
#             print("Weak password")
#             print("Please contain the digit  letter in your password")    

# problem 2
# take player names and run for the five player
# store them in a dictionary
# display -- highest score and average score 


# player={
#     "Rohit":20,
#     'Virat':150,
#     'Shubham':80,
#     'Rahul':110,
#     'Jadeja':90
# }
# Highest=player['Rohit']
# name="Rohit"
# total_score=0

# for i in player:
#     if player[i]>Highest:
#         Highest=player[i]
#         name=i
#     total_score +=player[i]


# print("Highest score=",Highest)
# print("Made by",name)
# print("total scor=",total_score)
# print("Average is =",total_score//5)



# ----------OR----------

# Highest=max(player.values())
# print("Highest score=",Highest)
# Sum=sum(player.values())
# average=Sum//5
# print("Average is ", average)



    # problem 3
# input two set of subject
# display
# common subject
# sunject only in first student
# sunject only in second student


# student_1=[]
# print("enter the 5 subject")
# for i in range(5):
#     name=input()
#     student_1.append(name)

# print("enter the 5 subject")
# student_2=[]
# for i in range(5):
#     name=input()
#     student_2.append(name)

# print("common subject is ",set(student_1) & set(student_2))
# print(" subject is only in s1 ",set(student_1) - set(student_2))
# print("subject is only in s2 ",set(student_2) - set(student_1))



# problem 4
# finnd the character that appear the maximum number of times in a String
# ignore the space


words="Python is the most amazing programminng language aa"
word=words.lower()
list={}
for i in words:
    if i in " ":
        continue
    if i not in list:
        list[i]=1
    else:
        list[i]+=1   

maxi=list["p"]
for j in list:
    if maxi < list[j]:
        char=j
        maxi=list[j]
print("maximum number of time charcter in the string is->",char,"=",maxi,'times')

for k,v in list.items():
    print(k,v)

  