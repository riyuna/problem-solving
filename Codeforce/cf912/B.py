import sys
input = sys.stdin.readline
for _ in ' '*int(input()):
	n=int(input())
	L=[]
	for j in range(n):L.append(list(map(int,input().split())))
	M=[(1<<30)-1]*n
	for i in range(n):
		for j in range(n):
			if i==j:continue
			else:
				M[i]&=L[i][j]
	check=True
	for i in range(n):
		for j in range(n):
			if i==j:continue
			if M[i]|M[j]!=L[i][j]:check=False
	if check:
		print('YES')
		for i in M:print(i,end=' ')
		print()
	else:
		print('NO')