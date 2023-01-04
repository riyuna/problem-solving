from copy import deepcopy
n,m=map(int,input().split())
mod=998244353
half=pow(2, mod-2, mod)

def mulmtx(L1, L2, mod):
	n=len(L2)
	res=[[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				res[i][j]+=L1[i][k]*L2[k][j]
				res[i][j]%=mod
	return res

def mtxpow(L, n):
	if n==1:return L
	M=mtxpow(L, n//2)
	MM=mulmtx(M, deepcopy(M), mod)
	if n%2==0:return MM
	else:return mulmtx(MM, L, mod)

if m>n:n,m=m,n

if n%4 or m%4:print(0)
elif m==4:
	print((2*pow(3, (n//4)-1, mod))%mod)

elif m==8:
	M=mtxpow([[18, 9], [16, 14]], (n//4)-1)
	res=(2*(M[0][0]+M[0][1])+M[1][0]+M[1][1])%mod
	res*=pow(half, (n//4)-2, mod)
	print(res%mod)

elif m==12:
	M=mtxpow([
		[108, 54, 0, 54, 27], 
		[96, 84, 0, 48, 42], 
		[96, 48, 12, 48, 48], 
		[96, 48, 0, 84, 42],
		[80, 64, 8, 64, 96]]
		, (n//4)-1)
	res=sum(M[0])*4+sum(M[1])*2+sum(M[3])*2+sum(M[4])
	res%=mod
	res*=pow(half, 2*(n//4)-3, mod)
	print(res%mod)

else:print(0)