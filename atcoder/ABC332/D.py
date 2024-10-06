import sys
input=sys.stdin.readline
from itertools import permutations
# for i in permutations([1,2,3,4,5], 5):print(i)
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
h,w=linput()
L1=[]
L2=[]
for i in ' '*h:L1.append(linput())
for i in ' '*h:L2.append(linput())
trL2=[[None]*h for i in range(w)]
for i in range(h):
	for j in range(w):
		trL2[j][i]=L2[i][j]
perm1=list(permutations(L1, len(L1)))
count=[0,1,1,2,2,3,1,2,2,3,3,4,2,3,3,4,4,5,3,4,4,5,5,6]
res=10**9
for i in range(len(perm1)):
	M=perm1[i]
	trM=[[None]*len(M) for i in range(len(M[0]))]
	for ii in range(len(M)):
		for jj in range(len(M[0])):
			trM[jj][ii]=M[ii][jj]
	perm2=list(permutations(trM, len(trM)))
	for j in range(len(perm2)):
		M2=perm2[j]
		flag=True
		for ii in range(h):
			for jj in range(w):
				if trL2[jj][ii]!=M2[jj][ii]:
					flag=False
					break
		if flag:
			result = count[i%24]+i//24+count[j%24]+j//24
			res=min(result, res)
if res==10**9:print(-1)
else:print(res)


# 3 3
# 0 0 1
# 0 0 0
# 1 0 0
# 1 0 0
# 0 0 0 
# 0 0 1