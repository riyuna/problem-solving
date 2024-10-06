import sys
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
n=iinput()
L=linput()
a=0
b=0
L.sort(reverse=True)
for i in range(n):
	if i%2:b+=L[i]
	else:a+=L[i]
print(a-b)