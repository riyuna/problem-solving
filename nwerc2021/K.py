n=int(input())
d=dict()
for _ in ' '*n:
	i,j,k=input().split()
	k=int(k)
	if i not in d:
		d[i]=[0,0,0]
	if j=='left':d[i][0]=k
	if j=='right':d[i][1]=k
	if j=='any':d[i][2]=k

pos=False
res=0

for i in d:
	L=d[i]
	if (L[0] and L[1]) or L[2]>1:pos=True
	res+=max([L[0],L[1],1])

if not pos:print("impossible")
else:print(res+1)