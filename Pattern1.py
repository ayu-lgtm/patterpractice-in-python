x = int(input("enter number :"))
p=2*x+1
q=2*x/2
for i in range(0,p):
    for j in range(0,p):
        if j < abs(q-i) or j > abs(q+i):
            print("*",end=" ")
        elif i > q and j > q and j+i-p >=q:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\b")