n,m=map(int,input().split())
c=0
L=[0]*m
L[0]+=1
for i in list(map(int,input().split())):
    c+=i
    c%=m
    L[c]+=1
res=0
for i in L:
    res+=(i*(i-1))//2
print(res)