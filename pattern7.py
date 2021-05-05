x = int(input())
p=x//2
for i in range(0,x//2):
    k=1
    for j in range(0,x):
        if j<=p+i and j>=p-i:
            print(k,end=" ")
            k=k+1
        else:
            print(" ",end=" ")
    print()