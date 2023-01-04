import sys
input = sys.stdin.readline
n,q=map(int,input().split())
s=input().strip()

L = [[0, 0, 0] for i in range(n+1)]

for j in range(3):
	onhere = True
	added = False
	viewed = ''
	for i in range(n):
		k = L[i][j]
		if s[i] == 'ABC'[j]:
			onhere=True
			viewed = ''
			L[i+1][j]=k
			continue
		if onhere:
			onhere=False
			viewed = s[i]
			L[i+1][j]=k+1
			continue
		if viewed == s[i] or added:
			L[i+1][j]=k
			continue
		viewed = ''
		added=True
		L[i+1][j]=k+1
print(L)
for i in ' '*q:
	l,r=map(int,input().split())
	a = L[r][0] - L[l-1][0]
	b = L[r][1] - L[l-1][1]
	c = L[r][2] - L[l-1][2]
	print(min([a,b,c]))