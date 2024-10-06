import sys
input=sys.stdin.readline
def linput():return list(map(int,input().split()))
n,s,m,l=linput()
L=[10**10]*120
L[0]=0
for i in range(120):
	if i+6<120:L[i+6]=min(L[i]+s,L[i+6])
	if i+8<120:L[i+8]=min(L[i]+m,L[i+8])
	if i+12<120:L[i+12]=min(L[i]+l,L[i+12])
res=10**10
for j in range(n, 120):
	res=min(res,L[j])
print(res)