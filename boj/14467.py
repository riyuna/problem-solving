n=int(input())
d=dict()
ct=0
for i in ' '*n:
	a,b=map(int,input().split())
	if a not in d:d[a]=b
	else:
		if d[a]!=b:
			d[a]=b
			ct+=1
print(ct)