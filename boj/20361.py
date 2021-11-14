import sys
input=sys.stdin.readline
n,x,k=map(int,input().split())
L=[0]*n
L[x-1]+=1
for i in range(k):
    a,b=map(int,input().split())
    L[a-1],L[b-1]=L[b-1],L[a-1]
for i in range(n):
    if L[i]:print(i+1)