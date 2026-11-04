import os 
path="c:\\Users\\hp\\Desktop\\python_devops\\python_advanced\\test"
print(list(os.walk(path)))


# $  python autom4.py 
# [('c:\\Users\\hp\\Desktop\\python_devops\\python_advanced\\test', ['inside_test'], ['hello.txt', 'hello2.txt'])
# , ('c:\\Users\\hp\\Desktop\\python_devops\\python_advanced\\test\\inside_test', [], ['insider_file'])]


 # path , [directories], [files]
 # then recursively goes for each directory and returns the same structure for each directory



 # tuples
x=(3,4,5)
print(x)
y,z,w=x
print(y)
print(z)
print(w)
