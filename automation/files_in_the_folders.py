import os 
folders=input("enter all the folders u want to list files of (space seperated): ").split()
for folder in folders:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print(f"folder {folder} not found")
        break
    except PermissionError:
        print(f"permission denied for folder {folder}")
        break
    print(f"files in {folder} are: ")
    for file in files:
        print(file)
