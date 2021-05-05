x = int(input())
p=x//2
for i in range(0,x//2+1):
    for j in range(0,x):
        if j%2==0 and i%2==0 and (j>=p-i and j <= p+i):
            print("*",end=" ")
        elif j%2!=0 and i%2!=0 and (j>=p-i and j<=p+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()