n=int(input())
L=list(map(int,input().split()))
ans=0
mem=0
ct=0
for i in range(n):
	if mem<L[i]:
		ct=0
		mem=L[i]
	else:
		ct+=1
		ans=max(ct,ans)
print(ans)