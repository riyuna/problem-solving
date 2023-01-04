n=int(input())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))

mem = 10**18
ans=[-1,-1]
for i in range(n):
	mxm=0
	for j in range(n):
		mxm = max(mxm, (L[i][0]-L[j][0])**2+(L[i][1]-L[j][1])**2)
	if mxm<mem:
		mem=mxm
		ans = L[i]

print(ans[0], ans[1])