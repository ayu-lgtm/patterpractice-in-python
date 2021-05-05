x = int(input())
p=x//2
for i in range(0,x//2):
    k=2
    for j in range(0,x):
        if j==p:
            print(0,end=" ")
        elif j>=p-i and j <=p+i and j!=p and j<p:
            print(j,end=" ")
        elif j>=p-i and j <=p+i and j!=p and j>p:
            print(j-k,end=" ")
            k=k+2
        else:
            print(" ",end=" ")
    print()