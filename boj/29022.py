import sys
input=sys.stdin.readline
from math import gcd
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

while True:
	a,b=linput()
	if a==b==0:break
	g=gcd(a,b)
	a//=g
	b//=g
	if a==1:
		print(0, 1)
		continue
	k1=pow(b,-1,a)
	k1*=(a-1)
	k1%=a
	k2=(b*k1+a-1)
	k2//=a
	if k1*2<a:print(k1, k2)
	else:print(a-k1,b-k2)