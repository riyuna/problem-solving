import sys
input = sys.stdin.readline
for i in ' '*int(input()):
	n,m=map(int,input().split())
	L1=list(map(int,input().split()))
	L2=list(map(int,input().split()))
	L=L1[::-1]
	res=[]
	L2.sort()
	pt=0
	while pt<m and L2[pt]<=L[0]:
		res.append(L2[pt])
		pt+=1
	for i in L:
		while pt<m and L2[pt]<=i:
			res.append(L2[pt])
			pt+=1
		res.append(i)
	if pt<m:
		for i in range(pt, m):
			res.append(L2[i])
	res.reverse()
	for i in res:print(i,end=' ')
	print()