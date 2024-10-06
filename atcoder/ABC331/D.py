import sys
input=sys.stdin.readline
def linput():return list(map(int,input().split()))
n,q=linput()
L=[]
for i in ' '*n:L.append(input().strip())
ctL=[[0]*(n+1) for i in range(n+1)]
for i in range(n):
	for j in range(n):
		ctL[i+1][j+1]=ctL[i+1][j]+ctL[i][j+1]-ctL[i][j]+int(L[i][j]=='B')
def solve(i, j):
	ii=i//n
	jj=j//n
	ri=i%n
	rj=j%n
	res=0
	res+=ii*jj*ctL[-1][-1]
	res+=ii*ctL[-1][rj]
	res+=jj*ctL[ri][-1]
	res+=ctL[ri][rj]

	return res
for _ in ' '*q:
	a,b,c,d=linput()
	print(solve(c+1,d+1)-solve(a,d+1)-solve(c+1,b)+solve(a,b))