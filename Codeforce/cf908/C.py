import sys
input = sys.stdin.readline
for i in ' '*int(input()):
	n,k=map(int,input().split())
	L=list(map(int,input().split()))
	pt=n-1
	flag=True
	if n>k:
		for i in range(k):
			if L[pt]>n:
				flag=False
				break
			pt-=L[pt]
			pt%=n
	else:
		for i in range(n):
			if L[pt]>n:
				flag=False
				break
			pt-=L[pt]
			pt%=n
			if pt==n-1:
				flag=True
				break
	print('YNeos'[not flag::2])