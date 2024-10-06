import sys
from bisect import bisect
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
#print('なんでや!阪神関係ないやろ!')

n,q=linput()
L=linput()
L.sort()
M=[0]
for i in L:
	M.append(M[-1]+i)

for i in ' '*q:
	k=iinput()
	print(bisect(M,k)-1)