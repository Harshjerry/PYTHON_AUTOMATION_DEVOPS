arn = "arn:aws:iam::123456789012:role/MyTestRole"
print(arn.split("/")) 
# Output ['arn:aws:iam::123456789012:role', 'MyTestRole']
print(arn.split("/")[1])
 #MyTestRole

name="Harshdeep Singh"
print(name.upper())   #HARSHDEEP SINGH
print(name.lower())  #harshdeep singh
print(len(name))      #15

num1=10
num2=20
sum=num1+num2
print(sum)  #30
product=num1*num2
print(product)  #200
difference=num1-num2
print(difference)  #-10
quotient=num1/num2
print(quotient)  #0.5
