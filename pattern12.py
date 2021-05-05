x=int(input("enter number:"))
for i in range(0,x):
    for j in range(1,x-i+1):
        print(" ",end=" ")
    for j in range(0,i+1):
        if j==0 or i==0:
            n=1
        else:
            n=n*(i-j+1)//j
        print(n,end=" ")
    print()