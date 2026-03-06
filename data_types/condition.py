import sys
type=sys.argv[1]
if type == 't2.micro':
    print("t2.micro is the smallest instance type available in AWS EC2.")
elif type == 't2.small':
    print("t2.small is a small instance type available in AWS EC2.")
else:    print("The instance type you entered is not recognized.")