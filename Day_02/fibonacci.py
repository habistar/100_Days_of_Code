def main():
    size = int(input("enter the size of the series\n"))
    n1 = 0
    n2 = 1
    count = 2
    print("the fibonacci series of size " + str(size) + " is:\n")
    print(n1)
    print(n2)
    while(count<size):
        t = n1 + n2
        count += 1
        print(t)
        n1 = n2
        n2 = t


main()