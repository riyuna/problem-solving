import sys
input=sys.stdin.readline
pL=[True]*320
pList=[]
pL[0]=False
pL[1]=False
for i in range(2, 320):
	if pL[i]==False:continue
	pList.append(i)
	for j in range(i*2, 320, i):
		pL[j]=False
bigpL=[True]*(10**5+1)
bigpL[0]=False
bigpL[1]=False
bigprimes=[]
for i in range(2, 10**5+1):
	if bigpL[i]==False:continue
	if i>316:bigprimes.append(i)
	for j in range(i*2, 10**5+1, i):
		bigpL[j]=False

rem=[0]*(10**5+1)
d=dict()
for i in pList:
	for j in range(i, 10**5+1, i):
		rem[j]=i

for i in pList:
	d[i]=[0,0]
	for j in range(2, 10**5+1):
		if rem[j]<=i:
			d[i].append(d[i][-1]+1)
		else:d[i].append(d[i][-1])

def solve(n,k):
	if k<317:
		for i in range(len(pList)-1):
			if pList[i]<=k<pList[i+1]:
				p=pList[i]
				return d[p][n]
	res=n-1
	for p in bigprimes:
		if p>n:return res
		if p>k:res-=(n//p)
	return res

for _ in ' '*int(input()):
	n,k=map(int,input().split())
	print(solve(n,k))