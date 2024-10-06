import sys
from collections import deque
from bisect import bisect_right
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

L=[True]*(1000001)
L[0]=False
L[1]=False
pL=[]
for i in range(2, 1000001):
	if not L[i]:continue
	for j in range(i*2, 1000001, i):
		L[j]=False
	pL.append(i)
mem=[]
for i in range(len(pL)):
	for j in range(i+1, len(pL)):
		a,c=pL[i],pL[j]
		res=a*a*c*c
		if res>10**12:break
		mem.append([res,i,j])
mem.sort()
n=iinput()
ct=0
for k,a,c in mem:
	if k*2>n:break
	cand=n//k
	pt=bisect_right(pL,cand)
	ct+=max(0, min(c, pt)-a-1)
print(ct)