n=int(input())
L=[0]*n
for i in range(n):
	a,b=map(int,input().split())
	L[i]=b
	for j in ' '*a:
		M=list(map(int,input().split()))
		