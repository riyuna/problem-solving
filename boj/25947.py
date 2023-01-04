n,b,a=map(int,input().split())
psum=[0]
L=list(map(int,input().split()))
L.sort()
for i in L:
	psum.append(psum[-1]+i)

res=0
for i in range(n+1):
	j = i-a
	if j<0:j=0
	if psum[i]+psum[j]>b*2:
		break
	res=i

print(res)