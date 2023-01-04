L=input().split()
d=dict()
check=True
for i in L:
	if i in d:check=False
	d[i]=True
print(['no','yes'][check])