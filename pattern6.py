x = int(input("enter number:"))
p=x//2
for i in range (0,x//2+1):
    for j in range(0,x+1):
        if(i%2==0 and j%2==0 and j>=p-i and j<=p+i):
            print("1",end=" ")
        elif(i%2!=0 and j%2!=0 and j>=p-i and j<=p+i):
            print("2",end=" ")
        else:
            print(" ",end=" ")
    print()