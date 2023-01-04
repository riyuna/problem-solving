import sys
input=sys.stdin.readline
n,k=map(int,input().split())
d=dict()
for i in range(k):
	s=input().strip()
	d[s]=i
L=[]
for i in d:
	L.append((d[i], i))
L.sort()
# print(L)
for i in range(min(n,len(L))):print(L[i][1])