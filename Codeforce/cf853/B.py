import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
    n=int(input())
    s=input().strip()
    L=[0]*n
    for i in range(n//2):
        if s[i]!=s[-i-1]:L[i]=1
    seg=L[0]
    for i in range(n):
        if i and L[i-1]==0 and L[i]==1:seg+=1
    if seg>1:print('No')
    else:print('Yes')