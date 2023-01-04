import sys
input=sys.stdin.readline
mod=10**9+7
n=int(input())
res=0
for i in ' '*n:
	c,k=map(int,input().split())
	c*=k
	k-=1
	res+=(c*pow(2,k,mod))
	res%=mod
print(res)