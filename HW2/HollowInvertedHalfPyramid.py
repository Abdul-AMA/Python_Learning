n = int(input("Enter number: "))



for i in range(0,n):
    print("*" , end = "")
print()

for i in range (0,n-2):
    print("*" , end = "")
    for j in range(0,n-i-3):
        print(" ", end="")
    print("*" , end = "")
    print()


print("*")