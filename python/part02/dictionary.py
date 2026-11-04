# ----dictionary store the data with the key and value
# --- left wala key hai and right wala value hai

student={
    "name":"akash",
    'age':23,
    'CGPA':8.5,
    'CITY':"banaras"
}

# print(student)
# print(type(student))
# print(student["name"])
# print(student["CGPA"])

# ---length----
# print(len(student))

# # ----------- updating the value-----------------
# student["name"]="vikash"
# print(student)

# ---OR----------
# student.update({ 'name':" Ram" ,'age': 25 })
# print(student)

# # ----inserting more key value--------

# student["state"]="UP"
# student['country']="India"
# print(student)
# # print(student["address"]) # it will give error

# #  ----- another method to accessing the key--

# # The .get() method retrieves the value associated with a key. 
# # It's similar to the bracket notation that we just used,
# #  but its advantage is that you can set a default value,
# #  so you won't get an error if the key doesn't exist:

# print(student.get('age'))

# print(student.get('address', "key is not found"))
# print(student.get('name', "key is not found"))

# # --------pop--------
# print(student.pop("state"))
# print(student)
# print(student.pop("state")) # it will give error becuse ab to state exits hi nhi krta hai hme phle hi pop kr diya hai


# loop over dictionary

# student={
#     "name":"akash",
#     'age':23,
#     'CGPA':8.5,
#     'CITY':"banaras"
# }

# for k in student.keys():
#     print(k)
# for k in student.values():
#     print(k)
# # ----or----
# for k in student.keys():
#     print(student[k])    

# # ---The .items() method returns a view object with all the key-value pairs in the dictionary, 
# # including both the keys and the values:


# for k in student.items():  # basicaly tuple me convert kr deta hai
#     print(k)   
# ---or------ 
# for k,i in student.items():
#     print(k,i)

# student.clear()    
# print(student)

# --code likhna hai employee ka salary 10% extra kr ke
# employee={
#     'salary':50000
# }
# employee['salary']+=(10/100)*employee['salary']
# # or --  employee['salary']=employee['salary']*1.10  (common le kr kiya hu)

# print(employee['salary'])

   #------Using enumerate() to Track a Counter or index
for i in enumerate(student):
    print(i)

print()

for i in enumerate(student.keys()):
    print(i)

print()

for i in enumerate(student.values()):
    print(i)    
print()

for i in enumerate(student.items()):
    print(i)