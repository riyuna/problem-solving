import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n,a,b=linput()
ct=0
def check(n):
	ct=0
	while n:
		ct+=(n%10)
		n//=10
	return ct
for i in range(1, n+1):
	if a<=check(i)<=b:ct+=i
print(ct)