n=int(input())
L=list(map(int,input().split()))
L.sort(reverse=True)
d=[1]+[0]*n

def get_expect(L, k):
	res=0
	for i in range(1, k+1):
		res+=L[i]*(i**(i/k))
	return res

result=0

for i in range(n):
	newd=[0]*(n+1)
	for j in range(n+1):
		if j:newd[j]+=d[j-1]*(L[i]/100)
		newd[j]+=d[j]*(1-L[i]/100)
	d=newd
	result=max(result, get_expect(d, i+1))

print(result)