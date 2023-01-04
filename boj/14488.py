from decimal import Decimal as D
n,t=map(D,input().split())
t=D(t)
L1=list(map(D,input().split()))
L2=list(map(D,input().split()))

lo=-1000000000
hi=1000000000

for i in range(int(n)):
	lo = max(lo, L1[i]-L2[i]*t)
	hi = min(hi, L1[i]+L2[i]*t)

print(int(lo<=hi))