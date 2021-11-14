a=int(input())
b=int(input())
c=int(input())
res=a*b*c
L=[0]*10
for i in str(res):
    L[int(i)]+=1
for i in L:print(i)