def solve(n):
	L=[0]*19
	L[0]=1
	for i in range(18):
		M=[]
		for j in range(18):
			if j==0:M.append(L[0]*(1-n/100))
			else:
				M.append(L[j-1]*n/100+L[j]*(1-n/100))
		L=M
	return L
a=int(input())
b=int(input())
ap=0
bp=0
aL=solve(a)
bL=solve(b)
for i in [2,3,5,7,11,13,17]:
	ap+=aL[i]
	bp+=bL[i]
print(1-(1-ap)*(1-bp))