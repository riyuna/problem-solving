from itertools import permutations
def check(L):
	n=len(L)
	for i in range(n):
		for j in range(n):
			if L[i][j]!=L[j][i]:return False
	return True

l,n=map(int,input().split())
L=[]
for i in ' '*n:L.append(input())
L.sort()
perm=permutations(L, l)
possible=False
res=0
for i in perm:
	if check(i):
		possible=True
		res=i
		break
if not possible:print('NONE')
else:
	for j in res:print(j)