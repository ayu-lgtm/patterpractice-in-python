x = int(input("enter number : "))
for i in range(0,x+1):
    for j in range (0,x+1):
        if j > i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()