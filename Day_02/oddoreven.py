def iseven(a):
    if(a%2==0):
        return True
    else:
        return False

num = int(input("enter number: \n"))
if(iseven(num)):
    print("number is even")
else:
    print("numver is odd")

