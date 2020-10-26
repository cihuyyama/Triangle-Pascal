n=int(input("How Long ?:"))
z=1
x=1
y=1
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        for k in range(1,i+1):
            z =z*k
        for k in range(1,j+1):
            x =x*k
        for k in range(1,(i-j)+1):
            y=y*k
        print(int(z/(x*y)),end=" ")
        z=1
        x=1
        y=1
    print("\n")
