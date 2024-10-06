n=int(input())
L=list(map(int,input().split()))
mod=998244353
tot=sum(L)
M=[0]*n
for i in range(n-2, -1, -1):
	M[i]=M[i+1]+L[i+1]
ans1=0
ans2=0
inv4=pow(4,mod-2,mod)
inv3=pow(3,mod-2,mod)
inv2=pow(2,mod-2,mod)
for i in range(n):
	n,m=L[i], M[i]
	# print(n,m)

	k=(n*m)*inv2
	ans2+=(2*k*ans1)
	ans1+=k
	ans1%=mod
	ans2%=mod
	res=0
	res+=((n*(n-1)*m*(m-1))*inv4)
	res%=mod
	res+=((n*m**2+m*n**2-2*n*m)*inv3)
	res%=mod
	res+=((n*m)*inv2)
	res%=mod
	ans2+=res
	ans2%=mod

print(ans2)
