import sys
input=sys.stdin.readline

for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	L.sort(reverse=True)
	if L[0]==L[1]:
		pos=2
		while pos<n and L[pos]==L[1]:
			pos+=1
		if pos==n:
			print('NO')
			continue
		L[1],L[pos]=L[pos],L[1]
	print('YES')
	for i in L:print(i,end=' ')
	print()
	