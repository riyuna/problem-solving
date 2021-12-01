from collections import deque
def solve(n):
    L=[[0,0] for i in range(n)]
    if n==1:return 1
    q=deque([])
    q.append(1)
    L[1]=[-1, 1]
    d=dict()
    d[1]=True
    while True:
        a=q.popleft()
        b=(a*10)%n
        c=(a*10+1)%n
        if b not in d:
            q.append(b)
            d[b]=True
            L[b][0]=a
            L[b][1]=0
        if c not in d:
            q.append(c)
            d[c]=True
            L[c][0]=a
            L[c][1]=1
        if b*c==0:
            return L

for i in ' '*int(input()):
    n=int(input())
    L=solve(n)
    if L==1:print(1)
    else:
        res=[]
        a,b=L[0]
        print(1,end='')
        while a!=-1:
            res.append(b)
            a,b=L[a]
        for i in res[::-1]:print(i,end='')
        print()