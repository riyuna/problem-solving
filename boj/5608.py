import sys
input=sys.stdin.readline
n=int(input())
d=dict()
for i in ' '*n:
	a,b=input().split()
	d[a]=b
for j in ' '*int(input()):
	s=input().strip()
	if s in d:print(d[s],end='')
	else:print(s,end='')
