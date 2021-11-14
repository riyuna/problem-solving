from collections import deque
n=int(input())
L=list(map(int,input().split()))
res=[-1]*n
q=deque([])
for i in range(n-1, -1 ,-1):
    while len(q) and q[-1]<=L[i]:
        q.pop()
    if len(q):
        res[i]=q[-1]
    q.append(L[i])

for i in range(n):
    print(res[i], end=' ')