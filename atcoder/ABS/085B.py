import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n=iinput()
L=[]
for i in ' '*n:L.append(iinput())
L.sort(reverse=True)
M=[]
for i in L:
	if len(M)==0 or M[-1]!=i:M.append(i)
print(len(M))