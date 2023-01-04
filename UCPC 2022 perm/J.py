import sys
from math import gcd
input=sys.stdin.readline

n=int(input())
L=list(map(int,input().split()))
newL=sorted(L)


def isSquare(n):
	mn = 0
	mx = 10**9+1
	while mn<mx:
		mid = (mn+mx)//2+1
		k=mid*mid
		if k==n:return True
		if k>n:mx=mid-1
		else:mn=mid+1
	if mn**2==n or mx**2==n:return True
	else:return False

flag = True
for i in range(n):
	g=gcd(L[i], newL[i])
	if not isSquare(L[i]//g) or not isSquare(newL[i]//g):
		flag=False
		break

print(["NO", "YES"][flag])