x = int(input())
for i in range(0,x//2+1):
    for j in range(0,x):
        if j >= 2*i and j <=i+x//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()