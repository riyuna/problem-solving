n=int(input())
L=list(map(int,input().split()))
def solve(n, L):
	d=dict()
	for i in range(n):
		if L[i] in d:
			return(d[L[i]]+1, i+1)
		d[L[i]]=i
	L.sort()
	for i in range(10):
		for j in range(n):
			if i==j:continue
			if L[j]%L[i]==0:
				return(d[L[i]]+1, d[L[j]]+1)
	return (-1,-1)

a,b=solve(n,L)
print(a,b)