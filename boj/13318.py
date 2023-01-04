def multiple(d1, d2):
	res=dict()
	for i1 in d1:
		for i2 in d2:
			k=i1+i2
			if k not in res:res[k]=0
			res[k]+=d1[i1]*d2[i2]
	return res
res=dict()
res[0]=1
L=[
	(11437, 6189), (5450, 25999), (16300, 12066), (4471, 15566), (11801, 22207),
	(50582, 12874), (21401, 8080), (25655, 35436), (25056, 36880), (30660, 6484)
]
# M=[29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
# for i in range(10):
# 	a,b=L[i]
# 	print(pow(M[i], a, 10**9+7))
# 	print(pow(M[i], b, 10**9+7))
for a,b in L:
	d=dict()
	d[a]=1
	d[b]=-1
	d[0]=-1
	res=multiple(res, d)

s1='e'*(300000)
print(s1)

for i in range(300000):
	if i not in res:print('e',end='')
	else: print(chr(ord('e')+res[i]),end='')