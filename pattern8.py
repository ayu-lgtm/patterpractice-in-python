x = int(input())
p=x//2
k=0
for i in range(0,x//2):
    k=k+1
    for j in range(0,x):
        if j<p+i and j>p-i:
            print(0,end=" ")
        elif j==p+i or j==p-i:
            print(k ,end=" ")
        else:
            print(" ",end=" ")
    print()