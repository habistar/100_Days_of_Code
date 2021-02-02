def main():
    num = int(input("enter a number:\n"))
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    print("the factorial is:\n" , factorial)
    
main()
