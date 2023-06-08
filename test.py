if __name__ == "__main__":
    n=5
    p=66
    for i in range(n):
        for j in range(0,i+1):
            if(j==0):
                print("A",end="")
            else:
                print(chr(p),end='')
                p=p+1
        
        print()