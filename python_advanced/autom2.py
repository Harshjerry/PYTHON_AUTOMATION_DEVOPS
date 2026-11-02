import os
import sys
path=input("Enter the path of the file: ")
if os.path.exists(path):
    df=os.listdir(path)
else:
    print(f"{path} does not exist")
    sys.exit(1)     # if the path does not exist, exit the program with an error code
print(df)
'''
f1=os.path.join(path, df[0])
if os.path.isfile(f1):
    print(f"{f1} is a file")
else:
    print(f"{f1} is not a file")

'''
for i in df:
    f1=os.path.join(path, i)
    if os.path.isfile(f1):
        print(f"{f1} is a file")
    else:
        print(f"{f1} is not a file")

    
