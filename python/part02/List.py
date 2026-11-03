  #---list----
  # list is a collection of items which is ordered and changeable. 
  # In python list is written with square brackets.  
  # it stores multiple items in a single variable.and it is mutable.
  # stores data of different data types.

# marks=[10,20,30,40,50]
# print(marks)
# print(type(marks))
# marks[0]=100
#     #  updating the element  
# print(marks)
# print(len(marks))
    #  give lenth of the list

#         #-------------- assigning new value to the list
# marks.append(60)
#     # append() method adds an item to the end of the list.
# print(marks)
# marks.insert(1,15)
#     # insert () method inserts an item at the specified index.
# marks.remove(30)
#     # remove() method removes the first occurrence of the specified value.
# marks.pop()
#     # pop() method removes the item at the specified index, or the last item if no index is specified.
# print(marks)    
# print(marks[0])
# print(marks[-1])


     #----------------------   iterating over the list
# marks=[10,20,30,40,50]
# n=len(marks)
# for i in range(n):
#     print(marks[i])
  
     # -------or--
     
# for i in marks:
#   print(i)

          # Q=>write the code to print even index number

# marks=[10,20,30,40,50]
# n=len(marks)
# for i in range(n):
#      if i%2==0:
#        print(marks[i])          


    #  ----built in function

# marks=[10,20,30,40,50]
# n=len(marks)
# print(max(marks))
# print(min(marks))
# print(sum(marks))----
   #---reverse the list
# for i in range(n):
#     print(marks[n-1-i])


# sorted(marks)
# print(marks)
# marks.clear()
# print(marks)
# marks.extend([60, 70, 80])
# print(marks)


# print(sum(marks))



#  homework disccusion

 
# number=[1,2,3,4]
# for i in range(len(number)):
#     number[i]=number[i]+i
# print(number) 


names=['akash','sky','schine','poonam']
longest=names[0]
for name in names:
    if len(name)>len(longest):
        longest=name
print(longest)       


   # --- list slicing------


a=[5,7,4,8,2,1,9]
print(a[1:4])   # index 4 is not included and index 1 is included

print(a[2:5])
print(a[:4])
print(a[1:])
print(a[0:7:2])
print(a[7::-1])
print(a[::-1])