import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

m=iinput()
L=[]
while True:
	a,b=linput()
	if a==b==0:break
	if a>b:a,b=b,a
	L.append([a,b])

L.sort()
ct=0
pt=0
now=0
flag=True
while pt<len(L):
	newnow=now
	end=-1
	while pt<len(L) and L[pt][0]<=now:
		end=max(end,L[pt][1])
		pt+=1
	if end==-1:
		flag=False
		break
	now=end
	ct+=1
	if end>=m:break
if not flag or end<m:print(0)
else:print(ct)