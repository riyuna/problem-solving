def solve(n,a,b):
    if a>n//2+1 or b<n//2:return False
    if b==n//2 and a!=n//2+1:return False
    if a==n//2+1 and b!=n//2:return False
    res1=[]
    res2=[]
    for i in range(1, n+1):
        if i==a:res1.append(i)
        elif i==b:res2.append(i)
        else:
            if i*2>n:res1.append(i)
            else:res2.append(i)
    return res1+res2

for i in ' '*int(input()):
    n,a,b=map(int,input().split())
    L=solve(n,a,b)
    if not L:print(-1)
    else:
        for i in L:print(i,end=' ')
        print()