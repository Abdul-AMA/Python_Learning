
s = input("Enter the string: ")
x = True
for i in range(0,int(len(s)/2)):
    if(s[i] != s[len(s)-i-1]):
        x = False
        break

print(x)