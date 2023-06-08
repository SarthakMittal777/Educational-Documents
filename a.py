def decide(c):
    if(c==k):
        return True
    else:
        return False
x,k=int(input()),int(input())
c=x**3 + x**2 + x + 1
print(decide(c))