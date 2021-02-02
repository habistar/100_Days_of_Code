def main():
    num = int(input("enter a number:\n"))
    if(num%4==0):
        if(num%100==0):
            if(num%400==0):
                print("leap year\n")
            else:
                print("not a leap year\n")
        else:
            print("leap year\n")
    else:
        print("not a leap year\n")

main()

    
 