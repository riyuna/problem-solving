from itertools import combinations
m,n=map(int,input().split())
L=[0]*m
for i in ' '*n:
	a,b,c=map(int,input().split())
	L[a]-=c
	L[b]+=c

bitdp=[-1]*(2**m)
bitdp[0]=0
bitlist=[i for i in range(m)]

for i in range(1, m+1):
	comb=list(combinations(bitlist, i))
	for tup in comb:
		res=0
		mx=-1
		c=0
		for k in tup:
			c+=L[k]
			res^=2**k
		for k in tup:
			before=res^2**k
			mx=max(mx, bitdp[before])
		if c==0:mx+=1
		bitdp[res]=mx

print(m-bitdp[-1])