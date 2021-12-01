import bisect
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(input())
ban=[]
for i in range(m-1):
    for j in range(n-1):
        if L[j+1][i+1]=='.':
            if L[j][i+1]==L[j+1][i]=='X':
                ban.append(i+0.5)
                break
q=int(input())
for _ in ' '*q:
    if len(ban)==0:
        print('YES')
        continue
    x1,x2=map(int,input().split())
    x1-=1
    x2-=1
    if bisect.bisect(ban,x1)!=bisect.bisect(ban,x2):print('NO')
    else:print('YES')