import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

mod = 998244353
n,m,t = map(int, input().split())
# fact = [1]
# for i in range(1, 10000001):
# 	last = fact[-1]
# 	last*=i
# 	last%=mod
# 	fact.append(last)

# def comb(n, k):
# 	if k==0:return 1
# 	if k<0: return 0
# 	if n<k:return 0
# 	res = fact[n] * pow(fact[k], mod-2, mod) * pow(fact[n-k], mod-2, mod)
# 	return res%mod

M=list(map(int,input().split()))

q=int(input())
if t==1:
	start = [1, 1]
	for i in range(m):
		k = M[i]
		if k==0 or k==n:continue
		a,d = start
		newa = a + ((n-k)*k*d)%mod * pow(n, mod-2, mod)
		newa%=mod
		newd = d * (n**2-2*k*n-n+2*k**2)
		newd %= mod
		newd = newd * pow(n*(n-1), mod-2, mod)
		newd %= mod
		start = [newa, newd]
	for i in ' '*q:
		c = int(input())
		a,d = start
		res = a+d*(c-1)
		res %= mod
		print(res)

if t==2:
	start = [1, 3, 2]
	for i in range(m):
		k = M[i]
		if k==0 or k==n:continue
		a, d, t = start

		a1, a2, a3 = a, a+d, a+2*d+t
		ak1 = a+k*d+t*(k*(k-1))//2
		ak2 = ak1+d+t*k
		ak3 = ak2+d+t*(k+1)

		newa = k*a1 + (n-k)*ak1
		newa%=mod
		newa*=pow(n, mod-2, mod)
		newa%=mod
	
		newa2 = k*(k-1)*a2
		newa2 += k*(n-k)*ak1
		newa2 += k*(n-k)*a1
		newa2 += (n-k)*(n-k-1)*ak2
		newa2%=mod
		newa2 *= pow(n*(n-1), mod-2, mod)
		newa2%=mod

		newa3 = k*(k-1)*(k-2)*a3
		newa3 += k*(k-1)*(n-k)*(2*a2 + ak1)
		newa3 += k*(n-k)*(n-k-1)*(2*ak2 + a1)
		newa3 += (n-k)*(n-k-1)*(n-k-2)*ak3
		newa3%=mod
		newa3 *= pow(n*(n-1)*(n-2), mod-2, mod)
		newa3%=mod

		newb = (newa2-newa)%mod
		newt = (newa3-newa2-newb)%mod
		start = [newa, newb, newt]
		
	for i in ' '*q:
		c=int(input())
		a,d,t = start
		res = a+(c-1)*d + (c-1)*(c-2)*t//2
		res%=mod
		print(res)