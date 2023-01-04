mod=10**9+7
fact=[1]
for i in range(1, 3001):
	fact.append(fact[-1]*i%mod)

def comb(n,k):
	if k>n or k<0:return 0
	return (fact[n]*pow(fact[k],mod-2,mod)*pow(fact[n-k],mod-2,mod))%mod
def solve(n,i,j,x,y):
	if x>y:
		i,j,x,y = n-j+1, n-i+1,y,x
	
	res=0
	if y!=n:
		for k in range(i+1, j):
			res+= comb(x-1, i-1)*comb(y-x-1, n-x+i-j) * comb(n-y-1, j-k-1)
			res%=mod
		for k in range(j+1, n):
			res += comb(x-1,i-1)*comb(y-x-1,j-i-1) *comb(n-y-1, k-j-1)
			res%=mod
		
		return res
	else:
		if j==n:return 0
		res += comb(x-1,i-1)*comb(y-x-1,j-i-1)
		res%=mod
		return res
for i in ' '*int(input()):
	n,i,j,x,y=map(int,input().split())
	print(solve(n,i,j,x,y))