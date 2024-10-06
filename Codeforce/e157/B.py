import sys
input=sys.stdin.readline
for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	L.sort()
	res=[[0, 0]for i in range(n)]
	for i in range(2*n):
		res[i%n][i//n]=L[i]
	ct=0
	for i in range(n-1):
		a,b=res[i]
		c,d=res[i+1]
		ct+=abs(a-c)+abs(b-d)
	print(ct)
	for a, b in res:print(a,b)