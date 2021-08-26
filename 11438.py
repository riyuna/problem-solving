import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
m=n
mx=0
while m:
    mx+=1
    m//=2
L = [[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    L[a].append(b)
    L[b].append(a)

parents = [0]*(n+1)
depth = [0]*(n+1)
check = [0]*(n+1)

deq = deque()
deq.append(1)
while len(deq):
    x=deq.popleft()
    check[x]=1
    for i in L[x]:
        if not check[i]:
            deq.append(i)
            parents[i]=x
            depth[i]=depth[x]+1

dp=[[0]*(mx+1) for i in range(n+1)]
for i in dp:print(i)
for i in range(n+1):dp[i][0]=parents[i]
for i in range(1,mx):
    for j in range(1,n+1):
        dp[j][i]=dp[dp[j][i-1]][i-1]

def solve(a,b):
    if depth[a]>depth[b]:a,b=b,a
    d=depth[b]-depth[a]
    for i in range(mx):
        if d&(2**i):b=dp[b][i]
    if a==b:return a
    for i in range(mx-1,-1,-1):
        if dp[a][i]!=dp[b][i]:
            a=dp[a][i]
            b=dp[b][i]
    return dp[b][0]
for i in ' '*(int(input())):
    a,b=map(int,input().split())
    print(solve(a,b))