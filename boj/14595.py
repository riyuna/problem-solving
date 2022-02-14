import sys
input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*int(input()):
    a,b=map(int,input().split())
    L.append([a,b])
L.sort()
res=n
l=0
r=0
for a,b in L:
    if r<a:
        res-=(r-l)
        l,r=a,b
    else:
        r=max(r, b)
res-=(r-l)
print(res)