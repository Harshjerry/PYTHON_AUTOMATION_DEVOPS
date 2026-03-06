import modules_defined as m 
import sys
import os
# num1=sys.argv[1]     wont work as it will be string and we need to convert it to int or float
# operation=sys.argv[2]
# num2=sys.argv[3]

num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])


if operation == "add":
    result = m.add(num1, num2)
    print(result)

#similary for  sensitibe  informaitonm we use env  variables
os.getenv("SECRET")
