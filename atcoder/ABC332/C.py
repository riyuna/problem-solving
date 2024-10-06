import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n,m=linput()
s=input().split('0')
res=0
for i in s:
	k=i.count('2')
	kk=i.count('1')
	if kk>m:k+=(kk-m)
	res=max(res,k)
print(res)