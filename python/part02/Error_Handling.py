# Common Python errors include 
# SyntaxError,
#  NameError,
#  TypeError, 
# IndexError, 
# and AttributeError ----etc


#Print("Hellow")  # that is called Name error

# print('hellow'   # SyntaxError

# if 10>7
#     print("hellow")   #SyntaxError


# if 10>7:
# print("hellow")  #IndentationError

# a=2
# b=0
# print(a/b)    #ZeroDivisionError


# li=[3,4,5]
# print(li[5])  #IndexError

 
#ge=int(input("Enter the age="))
# if put akash it will give ValueError


# print(5 + "5")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# num = 42
# num.append(5)
# AttributeError: 'int' object has no attribute 'append'













# try:
#     n=int(input("Enter the value of n="))
#     print(100/n)
# except:
#     print("💀 Some errror has occured")    

# except:
#     print("can not divided by  0")  
# but koi jaruri nhi hai 0 hi error ho kya pta hm input me string de tb

# yh iska disadvantage hai yh error ka type nhi btayga 

# -----------Catching Specific Error---

try:
  n=int(input("Enter the value of n="))
  print(100/n)

except Exception as e:
   print(e)
















