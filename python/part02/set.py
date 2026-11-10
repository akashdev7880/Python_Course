#-----Set----------------
# set is a collection which is unordered, unchangeable*, and unindexed.
#  In Python sets are written with curly brackets.
# it is the mutable data type but it does not allow duplicate values
# it store unique element

# student=[
#     'rahul','amit','akash','akash','vikash','rahul','amit'
# ]
# student1=[]
# for name in student:
#     if name not in student1:
#         student1.append(name)
# print(student1)        

# -------OR-------------------
# student={
#     'rahul','amit','akash','akash','vikash','rahul','amit'
# }
# print(student)
# # ======this is set



# print(type(student))
# print(len(student))

# num={1,3,5,2,6,8,1,4,75,3,2}
# print(len(num))
# # it will give 8 because it remove duplicate the element

# s={'akash',34, 34.3,False} 
# print(s)

# #--- creat the empty set--

# s=set()
# # adding the element in set
# s.add(5)
# s.add(23)
# print(s)

# # traversing the set

# for i in s:
#     print(i)

    # --remove the element in set

# s.remove(5)    
# print(s)
# print(s.remove(90))  # it will give error because 90 is not present in the given set


# item={1,2,3,4,5,6,8}
# combo=item.pop()
# print(combo)
# print(item.clear())




# # ------UNION----
# A={1,2,3,4,5}
# B={4,6,8,9,0}
# print(A|B)
# or print(A.union(B))

# # ---Intersection--------
# print(A&B)
# ---or
# print(A.intersection(B))


# # ---set diffrent----
# print(A-B)

# string to set
# text='banana'
# text2=set(text)
# print(text2)
# print(len(text2))

# com=[2,3,4,5,1,6,4,'akash','akash']
# com2=set(com)
# print(com2)
# print(len(com2))



# 