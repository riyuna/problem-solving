import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
	n,m,k=map(int,input().split())
	L=list(map(int,input().split()))
	bd = n//k
	res=n%k
	L.sort(reverse=True)
	check=True
	for i in L:
		if i==bd+1:
			if not res:
				check=False
				break
			res-=1
		if i>bd+1:
			check=False
			break
	print(['NO','YES'][check])