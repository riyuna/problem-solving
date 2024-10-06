n=int(input())
mem=dict()
ct=0
for i in range(1, 100000):
	res1=str(i)[:-1]+str(i)[::-1]
	res2=str(i)+str(i)[::-1]
	k1=int(res1)
	k2=int(res2)
	if k1 not in mem:
		mem[k1]=True
		if k1<=n:ct+=1
	if k2 not in mem:
		mem[k2]=True
		if k2<=n:ct+=1
print(ct)