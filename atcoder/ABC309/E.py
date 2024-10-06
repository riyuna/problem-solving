import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
L=list(map(int,input().split()))
ins=[]
for i in ' '*m:
    x,y=map(int,input().split())
    ins.append([x-1,y])
child=[[]for i in range(n)]
for i in range(n-1):
    child[L[i]-1].append(i+1)
check=[-1]*n
for x,y in ins:check[x]=max(check[x],y)
stack=deque()
stack.append(0)
while len(stack):
    now=stack.popleft()
    for i in child[now]:
        if check[now]-1>check[i]:
            check[i]=check[now]-1
        stack.append(i)
ct=0
for i in check:
    if i!=-1:ct+=1
print(ct)