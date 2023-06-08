# # def count_substring(string, sub_string):
# #     count=0
# #     for i in range(0,len(string)):
# #         if(len(string)>=1 and len(string)<=1):
# #             for j in range(0,len(sub_string)):
# #                 if(i==(sub_string)):
# #                     count=count+1 
# #     return count      
# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string)):
#         if string[i:i+len(sub_string)]==sub_string:
#             count+=1
#     return count
        

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# if __name__ == '__main__':
#     a={"sarthak":1234567890, "sam":8976543210,"krish":1234567898}
#     for i,j in a.items():
#         print(j)

# a={"sarthak":12, "samthak":98, "krish":76, "sam":78}
# ui=int(input("enter the roll number"))
# k=[]
# w=[]
# for i, j in a.items():
#     k.append(j)
#     w.append(i)
    
# for i in k:
#     for j in w:
#         if (ui==i):
#             print(k[0])


# a=int(input("how many students"))
# k=[]
# passed=[]
# for i  in range(0,a):
#     y=int(input("how many marks"))
#     k.append(y)
# for i  in k:
#     if i>=40:
#         passed.append(i)
# print(passed)

# term1=0
# term2=1
# n=int(input("how many terms"))
# print(0)
# for i in range(0,n):
#     next=term1+term2
#     term1=term2
#     term2=next
#     print(term2)

# n=int(input("number of iterartions"))
# o=int(input("number"))
# for i in range(0,n):
#     if(o%2==0):
#         a=o//2
#         print(y)
#     else:
#         b=3*o+1
#         print(b)

# n=int(input("how many people"))
# a={}
# x=[]
# y=[]
# for i in range(0,n):
#     d=input("enter the value birthday DD/MM/YY")
#     name=input("enter your name")
#     x.append(d)
#     y.append(name)
# print(x)
# print(y)
    
# for i in range(0,n):
#     for i in x:
#         for j in y:
#             a.update(key=j)
# print(a)
# a={"sarthak":"12/08/22","sam":"13/08/22","jijutsu":"14/12/22"}
# name=[]
# birth=[]
# for i,j in a.items():
#     name.append(i)
#     birth.append(j)
# for i in birth:
#     if(i[3:5]=="08"):
#         print(i)
# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# n=5
# for i  in range(0,n):
#     for j in range(i,n-1):
#         print(" ",end="")
#     for j in range(0,i):
#         print("*",end="")
#     for j in range(0,i+1):
#         print("*",end='')
#     print()
    
# for p in range(0,n):
#     for q in range(0,p):
#         print(" ",end="")
#     for q in range(p,n-1):
#         print("*",end='')
#     for q in range(p,n):
#         print("*",end="")
#     print()


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     sum=0
#     total=0.00
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     c=student_marks[query_name]
#     print(c)
#     for i in c:
#         sum=sum+i
#     total=sum/n
#     print(total)
   
#     print(student_marks.keys())
        
# a={"sarthak":[67,37,38]}
# print(a["sarthak"])  

# def summ(a):  
#     return a+2
# a=[1,2,3,4,5]
# sub=lambda a: a+2
# print(sub(2))

# n=3 
# for i  in range(0,n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(0,i):
#         print("*",end="")
#     for j in range(0,i+1):
#         print("*",end="")
#     print()
# for i  in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         print("*",end="")
#     for j in range(i,n):
#         print("*",end="")
#     print()



# n=5
# p=65
# for i  in range(0,n):
#     for j in range(i,n-1):
#         print(" ",end="")
#     for j in range(0,i+1):
#         if(j%2==0):
#             print(chr(67),end="")
#         else:
#             print("E",end="")
#     for j in range(0,i):
#         if(j%2==0):
#             print(chr(67),end="")
#         else:
#             print(chr(67+2),end="")
#     print()
    
# for p in range(0,n):
#     for q in range(0,p):
#         print(" ",end="")
#     for q in range(p,n-1):
#         print("*",end='')
#     for q in range(p,n):
#         print("*",end="")
#     print()

# a="WELCOME"
# b=len(a)
# n=5
# p=65
# k=0
# for i  in range(0,len(a)):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(0,i):
#         print("*",end="")
#     for j in range(0,i+1):
#         print("*",end="")
#     for j in range(0,i+1):
#         if(i==6):
#             print(a[k],end=" ")
#             k=k+1
#         else:
#             print("*",end="")
    
    # for j in range(0,i):
    #     if(j%2==0):
    #         print(chr(67),end="")
    #     else:
    #         print(chr(67+2),end="")
#     print()
# # for z in range(0,len(a)):
# #     print(a[k],end=" ")
# #     k=k+1
    
# for p in range(0,n):
#     for q in range(0,p):
#         print(" ",end="")
#     for q in range(p,n-1):
#         print("*",end=' ')
#     for q in range(p,n):
#         print("*",end=" ")
#     #     for j in range(0,i):
# #         print("*",end="")
# #     for j in range(0,i+1):
# #         print("*",end="")
#     print()


n=4
a="WELCOME"
b=len(a)
m=2
p=65
k=0
l=n*m
for i  in range(0,l):
    for j in range(i,l-1):
        print(" ",end="")
    for j in range(0,i):
        print(".",end="")
    for j in range(0,i+1):
        print(".",end="")
    print()
print(" W E L C O M E")
for p in range(0,l):
    for q in range(0,p):
        print(" ",end="")
    for q in range(p,l-1):
        print(".",end='')
    for q in range(p,l):
        print(".",end="")
    print()


