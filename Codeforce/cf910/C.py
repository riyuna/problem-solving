import sys
input=sys.stdin.readline
for i in ' '*int(input()):
	n,m,k=map(int,input().split())
	if k<(n+m-2) or (n+m-2-k)%2:
		print('NO')
		continue
	print('YES')
	ct=(n+m-2-k)
	resa=[['R']*(m-1) for i in range(n)]
	resb=[['R']*(m) for i in range(n-1)]
	for i in range(m-1):
		if i%2:
			resa[0][i]='B'
	if (n+m)%2==0:
		resa[-2][-1]='B'
		resa[-1][-1]='B'
	else:
		resb[-1][-2]='B'
	resb[0][0]='B'
	resb[0][1]='B'
	for i in range(n-1):
		if (m-1+i)%2:
			resb[i][-1]='B'
	for i in resa:
		for j in i:print(j,end=' ')
		print()
	for i in resb:
		for j in i:print(j,end=' ')
		print()