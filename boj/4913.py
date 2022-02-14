psum=[0,0]
psum2=[0,0]
pL=[True]*1000001
pL[0]=False
pL[1]=False
for i in range(2, 1000001):
	if not pL[i]:
		psum.append(psum[-1])
		psum2.append(psum2[-1])
		continue
	if i%4==3:
		psum.append(psum[-1]+1)
		psum2.append(psum2[-1])
	else:
		psum.append(psum[-1]+1)
		psum2.append(psum2[-1]+1)
	for j in range(i*2, 1000001, i):
		pL[j]=False

while True:
	l,r=map(int,input().split())
	if (l,r)==(-1,-1):break
	ll=max(l, 1)
	rr=max(r, 1)
	print(l, r, psum[rr]-psum[ll-1], psum2[rr]-psum2[ll-1])