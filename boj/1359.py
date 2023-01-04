n,m,k=map(int,input().split())
res=0
def fact(n):
	res=1
	for i in range(n):res*=(i+1)
	return res
def comb(n, k):
	if k<0 or k>n:return 0
	return fact(n)/fact(n-k)/fact(k)
for i in range(k, m+1):
	res += comb(m, i)*comb(n-m, m-i)/comb(n,m)

print(res)