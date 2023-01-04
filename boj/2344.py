n,m=map(int,input().split())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))

def solve(L, start, dir):
	while 0<=start[0]<len(L[0]) and 0<=start[1]<len(L):
		x,y = start
		if L[y][x]:
			dir[0],dir[1]=-dir[1],-dir[0]
		
		start = [x+dir[0], y+dir[1]]
	
	if start[0]==-1:return start[1]+1
	if start[0]==len(L[0]):return len(L)+len(L[0])+(len(L)-start[1])

	if start[1]==len(L):return start[0]+len(L)+1
	if start[1]==-1:return len(L)*2+len(L[0])+(len(L[0])-start[0])

for i in range(n):
	print(solve(L, [0,i], [1,0]), end=' ')

for i in range(m):
	print(solve(L, [i,n-1], [0,-1]), end=' ')

for i in range(n):
	print(solve(L, [m-1,n-i-1], [-1,0]), end=' ')

for i in range(m):
	print(solve(L, [m-i-1,0], [0,1]), end=' ')