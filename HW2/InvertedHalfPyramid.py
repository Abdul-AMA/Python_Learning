n = int(input("Enter number: "))

for i in range(0,n):
    for j in range(0,n-i):
        print("*" , end = " ")
    print()