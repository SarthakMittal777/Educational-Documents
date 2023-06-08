n=5
a="WELCOME"
b=len(a)
n=7
p=65
k=0
for i  in range(0,n):
    for j in range(i,n-1):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    for j in range(0,i+1):
        print("*",end="")
    print()
print("W E L C O M E")
for p in range(0,n):
    for q in range(0,p):
        print(" ",end="")
    for q in range(p,n-1):
        print("*",end='')
    for q in range(p,n):
        print("*",end="")
    print()


