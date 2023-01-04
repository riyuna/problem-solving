import sys
input=sys.stdin.readline

n,m=map(int,input().split())
mod=1000000007
L=[]
for i in range(m):L.append(list(map(int,input().split()))+[pow(3, i, mod)])
L=L[::-1]

p=[-1]*(n+1)
def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a

res=0
for a, b, c in L:
	if (find(0)==find(a) and find(n-1)==find(b)) or (find(0) == find(b) and find(n-1)==find(a)):
		res+=c
		res%=mod
	else:
		merge(a, b)

print(res)