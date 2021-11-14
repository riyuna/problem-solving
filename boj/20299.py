import sys
input=sys.stdin.readline
n,k,l=map(int,input().split())
L=[]
for i in ' '*n:
    a,b,c=map(int,input().split())
    if a>=l and b>=l and c>=l and a+b+c>=k:L.extend([a,b,c])
print(len(L)//3)
for i in L:print(i,end=' ')