n,c=map(int,input().split())
d=dict()
L=list(map(int,input().split()))
for i in range(n):
	if L[i] not in d:
		d[L[i]]=[0, i]
	d[L[i]][0]-=1

M=[]
for i in d:
	M.append((*d[i], i))
M.sort()

for a, b, c in M:
	for _ in range(-a):
		print(c, end=' ')