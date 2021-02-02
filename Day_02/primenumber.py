def main():
    num = int(input("enter a number to check:\n"))
    p = True
    for i in range(2, num):
        if(num%i==0):
            p = False
            break
    if(p):
        print("number is prime")
    else:
        print("number is not prime")

main()