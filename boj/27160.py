import sys
input=sys.stdin.readline
d=dict()
for i in ' '*int(input()):
	s,n=input().split()
	n=int(n)
	if s not in d:d[s]=0
	d[s]+=n

check=False
for i in d:
	if d[i]==5:check=True
print('YNEOS'[1-check::2])