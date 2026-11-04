             #  --- tuple -------
# tuple is the immutable list that means can not be change if they create one time 

days=('Monday','Tuesday','Wednesday','Thusday','Friday','Saturday','Sunday',1,1,2,3,4,5,6,7)

# print(type(days))
# print(days[1])
# print(days[8])
# print(len(days))
# print(days[-3])
#  slicing---------
# print(days[1:9])
# print(days[::-1])

# print("Monday"in days)
# print("monday"in days)

# -----------use built in funnction

# print(days.index(4))
# print(days.count(1))

# number=(23,45,12,66)
# print(max(number))
# print(min(number))
# print(sum(number))




# single=(1)
# print(type(single))  # it will give integer

# sing=(1,)
# print(type(sing))   # it will give tuple



# traversing the tuple-------

# for ele in days:
#     print(ele)
#  or
# n=len(days) 
# for ele in range(n):
#     print(days[ele])   


# ---------Packing and Unpacking----------


# student=('akash',8.5,23)


# # -----unpacking

# name,cgpa,age=student
# print(name)
# print(age)
# print(cgpa)
# print(name,age,cgpa)

# # -----packing

# def show():
#     return 2,3
# a=show()
# print(a)
