import sys
input=sys.stdin.readline
n=int(input())
adj=[0]*n
for i in range(n-1):
	L=list(input())
	for j in range(i+1):
		if L[j]=='1':adj[i+1]+=1
		else:adj[j]+=1
adj.sort()
res=0
ct=0
for i in range(n):
	ct-=i
	ct+=adj[i]
	res=max(res,ct)
print(res)