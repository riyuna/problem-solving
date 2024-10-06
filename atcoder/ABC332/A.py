import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n,s,k=linput()
res=0
for i in ' '*n:
	a,b=linput()
	res+=(a*b)
print(res+(0 if res>=s else k))