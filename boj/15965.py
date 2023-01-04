pL=[True]*8000001
pL[0]=False
pL[1]=False
p=[]
for i in range(2, 8000001):
	if not pL[i]:continue
	p.append(i)
	for j in range(i*2, 8000001, i):pL[j]=False

print(p[int(input())-1])