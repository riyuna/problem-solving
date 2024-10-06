from math import gcd
k,l,r=map(int,input().split())
mod=10**9+7
mem=dict()
def f(n,k,zero):
	if (n,k,zero) in mem:return mem[(n,k,zero)]
	res=0
	if k==1:
		res=n+1
	elif n<10:
		for i in range(n+1):
			if i%k==0:res+=1
	else:
		ct=0
		first=n
		while first>9:
			first//=10
			ct+=1
		other=n%(10**ct)
		if zero:
			res += 10**ct
		else:
			res += f(10**ct-1, k, False)
		for i in range(1, first):
			res+=f(10**ct-1, k//gcd(k, i), True)
		if other<(10**(ct-1)):
			res+=(other+1)
		else:
			res+=f(other, k//gcd(k,first), True)
	res%=mod
	mem[(n,k,zero)]=res
	return res
print((f(r,k,False)-f(l-1,k,False))%mod)
# print(mem)