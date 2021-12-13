import sys
input=sys.stdin.readline

for i in ' '*int(input()):
    n,a,b=map(int,input().split())
    if abs(a-b)>1 or a+b>n-2:
        print(-1)
        continue
    res=[]
    if a>b:
        for i in range(b):
            res.append(n-i)
            res.append(i+1)
        res.append(n-b)
        not_used=[b+1,n-b]
    elif a==b:
        for i in range(b):
            res.append(n-i)
            res.append(i+1)
        not_used=[b+1, n-b+1]
    else:
        for i in range(a):
            res.append(i+1)
            res.append(n-i)
        res.append(a+1)
        not_used=[a+2, n-a+1]
    l,r=not_used
    for i in range(l,r):
        if i==l:res=[i]+res
        else:
            if a>b:
                res.append(l+r-i)
            else: res.append(i)
    for i in res:
        print(i,end=' ')
    print()