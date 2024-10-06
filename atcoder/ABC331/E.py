import sys
input=sys.stdin.readline
def linput():return list(map(int,input().split()))
n,m,l=linput()
L1=linput()
L2=linput()
pairs=[]
for i in ' '*l:
	a,b=linput()
	pairs.append([a-1,b-1])
d1=dict()
d2=dict()
L11=[]
L22=[]
for i in range(n):
	L11.append([L1[i], i])
for i in range(m):
	L22.append([L2[i], i])
L11.sort()
L22.sort()
for i in range(n):
	a,b=L11[i]
	d1[b]=i
for j in range(m):
	a,b=L22[j]
	d2[b]=j
# print(d1)
# print(d2)
# print(L11)
# print(L22)
# print(pairs)
npairs=[]
for a,b in pairs:
	npairs.append([d1[a],d2[b]])
npairs.sort(reverse=True)
# print(npairs)
Lmax=[m-1]*n
for a, b in npairs:
	if Lmax[a]==b:Lmax[a]-=1
result=0
for i in range(n):
	if Lmax[i]==-1:continue
	result=max(result, L11[i][0]+L22[Lmax[i]][0])
# print(Lmax)
print(result)