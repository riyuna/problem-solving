import sys
from collections import deque
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()
L=linput()
less=[0]*(n+1)
more=[0]*(n+1)

for i in L:
	if i<=0:less[-i]+=1
	else:more[i]+=1
for i in range(1, n+1):
	more[i]+=more[i-1]
for i in range(n-1, -1, -1):
	less[i]+=less[i+1]

result=[]
for i in range(0, n+1):
	if more[i]+less[i]==(n-i):result.append(i)
print(len(result))
for i in result:print(i,end=' ')