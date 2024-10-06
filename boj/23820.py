d=dict()
n=int(input())
L=list(map(int,input().split()))
for i in L:
    d[i]=1
if 0 not in d:print(0)
elif 1 not in d:print(1)
else:
    mem=dict()
    for i in d:
        if i==0 or i==1:continue
        for j in range(1, 2100001//i+1):
            if j in d: mem[i*j]=1
    for i in range(2, 2100001):
        if i not in mem:
            print(i)
            break