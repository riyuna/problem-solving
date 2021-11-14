n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(input())
res=0
for i in range(n):
    inside=False
    for j in range(m):
        if L[i][j]=='/' or L[i][j]=='\\':
            res+=0.5
            inside=not inside
        else:
            res+=int(inside)
if res==int(res):print(int(res))
else:print(res)