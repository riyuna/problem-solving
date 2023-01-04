n=int(input())
L=[[0]*n for i in range(n)]
if n<5:print(-1)
else:
	L[n//2][n//2]=n
	L[n//2-1][0]=2
	L[n//2-1][n-1]=n-2
	L[n//2+1][0]=n-2
	L[n//2+1][n-1]=2
	for i in range(n//2-1):
		L[i][i+1]=n
		L[-i-1][-i-2]=n
	for l in L:
		for i in l:
			print(i,end=' ')
		print()