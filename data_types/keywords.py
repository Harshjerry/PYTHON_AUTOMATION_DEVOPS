num1=10
num2=20
#they are gloabal varaibles   scope global

def add():
     a=5
     b=num1
     return a+b

#here a and b are local variables scope local
 # if we use them outside the function it will give error because they are local variables and can only be accessed within the function where they are defined.
 