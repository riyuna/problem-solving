import sys
input = sys.stdin.readline

mod = 10**9+7
fact=[1]
invfact=[1]
for i in range(1, 4000001):
	fact.append((fact[-1]*i)%mod)
	invfact.append((invfact[-1]*pow(i,mod-2,mod))%mod)

def comb(n,k):
	if n<=0 or k<=0:return 1
	if n<k:return 0
	return (fact[n]*invfact[n-k]*invfact[k])%mod

while True:
	a,b,c,sx,sy=map(int,input().split())
	if a+b+c+sx+sy==0:break
	tot=0
	for w in range(max(a, b+sx-sy), sx+1):
		now=1
		wb = w-sx+sy
		if wb<0 or wb>sy:continue
		if (w==0 and a!=0) or (wb==0 and b!=0):continue
		if (a==0 and w>0) or (b==0 and wb>0):continue
		now*=comb(w-1, w-a)
		now*=comb(wb-1, wb-b)
		now*=comb(a+b+c+sx-w-1, sx-w)
		tot+=now
		tot%=mod
	tot*=(comb(a+b+c,a)*comb(b+c,b))
	print(tot%mod)