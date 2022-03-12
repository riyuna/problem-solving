import sys
input=sys.stdin.readline
n=int(input())
e=n*2

p=[-1]*n
def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a

d=dict()
for i in range(n):
	x,r=map(int,input().split())
	if x+r not in d:d[x+r]=i
	else:
		merge(d[x+r], i)
	if x-r not in d:d[x-r]=i
	else:
		merge(d[x-r], i)

c=0
for i in p:
	if i==-1:c+=1

v=len(d)

print(c+1-v+e)