# password=input("Enter the password=")
# if password=="hellow@123":
#     print("Welcom")
# else:
#     print("try again")   
# 
# num=0
# if num:
#     print("true")
# else:
#     print("false")    
# 
 

# coolest code in company
# mark=30
# if mark<30:
#     print("A")
# elif  mark <=70:
#     print("B")
# else:
#     print("C")

# use of loop

# p_language=["python","java","c++","c#"]
# for i in p_language:
#     print(i)

# # notes--Notice that the print(language) is indented inside of the loop. Without that indentation, you would get an IndentationError:

# # ---Looping through Other Iterables----
# for char in 'akash':
#     print(char)

# # ---Nesting for Loops----

# categories=['fruit', 'vegetable']
# food=['Apple', 'carrot','banana']
# for i in categories:
#     for j in food:
#         # print(food)
#         print(i,j)


# # use of while

# gift_Number=8
# guess=0
# while guess!=gift_Number:
#     guess=int(input("Enter the guess number in between (1-10)= "))
#     if guess!=gift_Number:
#         print("wrong! Try again")

# print("You win the the price")


# question

# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     for letter in word:
#         if letter.lower() in 'aeiou':
#             print(f"'{word}' contains the vowel '{letter}'")
#             break
#     else:
#         print(f"'{word}' has no vowels")


 # ------------concept of range-------------------
# rang(start,stop,step)
# for num in range(3):
#     print(num)

# for num in range(2,11,2):
#     print(num,end=" ")


# number=list(range(2,11,2))
# print(number)   

# ----printing hi 5 times using for loop it includes 0 to 4
# for num in range(5): 
#     print("hi") 

# for i in range(10,0,-1):
#     print(i)

# only using one parameter in range() function it will start from 0 to n-1
for i in range(10):
    print(10-i)



















# using of enumerate()function------

# language=['hindi','English','Spanish','Chanies']
# for i, j in enumerate(language):
#     print(f'Index {i} and language {j}')

    
# print(type(language))

        
# using of zip() function-----
# It is used to iterate over multiple iterables in parallel.


# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]
# for name,id in zip(developers,ids):
#     print(f'ID: {id}')
#     print(f'Name: {name}')
   
