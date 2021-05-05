x=int(input("enter number:"))
p=x-1
for i in range(0,x):
    for j in range (0,x):
        if j==p-i or j==p:
            print("*",end=" ")
        elif i==p:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()