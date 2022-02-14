import sys
mod=10**9+7
input=sys.stdin.readline
a,m=map(int,input().split())
mem=dict()
def length_check(n):
	ct=0
	while n:
		ct+=1
		n//=2
	return ct
def root(n):
	if n==0:return -1
	c=1
	while True:
		c*=2
		if c>n:
			c//=2
			break
	return n-c

for i in ' '*m:
	n=int(input())
	res=pow(2, a-length_check(n), mod)
	if n in mem:
		res-=mem[n]
		res%=mod
	print(res)
	k=n
	while k>=0:
		if k not in mem:mem[k]=0
		mem[k]+=res
		mem[k]%=mod
		k=root(k)
