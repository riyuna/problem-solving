import sys
input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*n:
    a,b=map(int,input().split())
    L.append([a,b])
L.sort()
res=0
l=-(10**10)
r=-(10**10)
for a,b in L:
    if r<a:
        res+=(r-l)
        l,r=a,b
    else:
        r=max(r, b)
res+=(r-l)
print(res)