import sys
input=sys.stdin.readline

n=int(input())
L=list(map(int,input().split()))
mod = 998244353
d=dict()
d[L[1]]=1
ct=1
for i in range(1, n-1):
	newd=dict()
	ct*=2
	if 0 in d:ct-=d[0]
	ct%=mod
	for j in d:
		if j-L[i+1] not in newd:newd[j-L[i+1]]=0
		if j+L[i+1] not in newd:newd[j+L[i+1]]=0
		newd[j-L[i+1]]+=d[j]
		newd[j-L[i+1]]%=mod
		if j!=0:
			newd[j+L[i+1]]+=d[j]
			newd[j+L[i+1]]%=mod
	# print(newd)
	d=newd
print(ct)