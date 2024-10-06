import sys
input = sys.stdin.readline
for i in ' '*int(input()):
	n,k=map(int,input().split())
	L=list(map(int,input().split()))
	if k==1:
		check=True
		for i in range(n-1):
			if L[i]>L[i+1]:check=False
	else:check=True
	print(['NO','YES'][check])