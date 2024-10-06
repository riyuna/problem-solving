import sys
from math import gcd
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n=iinput()
L=linput()
k=L[0]
for i in L:k=gcd(i,k)
ct=0
while k%2==0:
	ct+=1
	k//=2
print(ct)