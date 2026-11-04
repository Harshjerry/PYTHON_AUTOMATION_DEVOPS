
import os 
import sys
import time 
#delete file older than k days 
k=4
path=input("Enter the path of the Directory: ")
if os.path.exists(path):
    df=os.listdir(path)
else:
    print(f"{path} does not exist")
    sys.exit(1)     # if the path does not exist, exit the program with an error code

if os.path.isfile(path):
    print(f"{path} is a file")
    sys.exit(1)     # if the path is a file, exit the program with an error code
# for file in df:
#     f1=os.path.join(path, file)
#     if os.path.isfile(f1):
#         file_age= os.path.getatime(f1)  # get the last access time of the file
#         print(f"{f1} is a file, last accessed on {time.ctime(file_age)}")

for file in df:
    f1=os.path.join(path, file)
    if os.path.isfile(f1):
        file_age= os.path.getatime(f1)  # get the last access time of the file
        file_age_days= (time.time() - file_age) / (24 * 3600)  # convert seconds to days
        if file_age_days > k:
            os.remove(f1)  # delete the file
            print(f"{f1} is deleted")
        else:
            print(f"{f1} is not deleted")

