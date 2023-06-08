
# str89=input("ENTER YOU ROLL NUMBER")
# print("The department is =>",str89[0:2])
# print('The admisiion year is =>',str89[2:4])
# print("The degree is =>",str89[4:5])
# print("The position of class =>",str89[5:8])
# a=input("enter string")
# for j in a:
#     if(j=="a" or j=="e" or j=="i" or j=="o" or j=="u"):
#         print(j)
# #
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# def print_full_name(first, last):
#     print("Hello {} {}! You just delved into python.".format(first,last))
    

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

import string
def rangoli(n):
    L = []
    sarthak = string.ascii_lowercase # 
    for i in range(n):
        s = "-".join(sarthak[i:n])
        print(s)
        L.append((s[::-1]+s[1:]).center( 20,"-")) 
    print('\n'.join(L[:0:-1]+L))
    
    
n = int(input(""))
rangoli(n)