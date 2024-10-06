import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

h,w=linput()
L=[]
res=[0]*min(h,w)
for i in ' '*h:L.append(list(input().strip()))
dp1=[[0]*w for i in range(h)]
dp2=[[0]*w for i in range(h)]
dp3=[[0]*w for i in range(h)]
dp4=[[0]*w for i in range(h)]
for i in range(h):
	for j in range(w):
		if L[i][j]=='.':continue
		if i>0 and j>0:dp1[i][j]=dp1[i-1][j-1]+1
		else:dp1[i][j]=1
		if i>0 and j<w-1:dp2[i][j]=dp2[i-1][j+1]+1
		else:dp2[i][j]=1
for i in range(h-1, -1, -1):
	for j in range(w):
		if i<h-1 and j>0:dp3[i][j]=dp3[i+1][j-1]+1
		else:dp3[i][j]=1
		if i<h-1 and j<w-1:dp4[i][j]=dp4[i+1][j+1]+1
		else:dp4[i][j]=1

for i in range(1, h-1):
	for j in range(1, w-1):
		if L[i][j]==L[i-1][j-1]==L[i-1][j+1]==L[i+1][j-1]==L[i+1][j+1]=='#':
			res[min([dp1[i][j], dp2[i][j], dp3[i][j], dp4[i][j]])-2]+=1
for i in res:print(i,end = ' ')