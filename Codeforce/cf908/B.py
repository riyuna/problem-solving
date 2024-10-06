import sys
input = sys.stdin.readline
for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	d=dict()
	for i in L:
		if i not in d:d[i]=0
		d[i]+=1
	ct=0
	for i in d:
		if d[i]>1:ct+=1
	if ct<2:
		print(-1)
		continue
	M=[]
	a=0
	b=0
	for i in d:
		if d[i]>1:
			if not a:a=i
			else:b=i
		if b:break
	pt1=0
	pt2=0
	for i in L:
		if i==a:
			if pt1%2==0:
				M.append(1)
			else:M.append(2)
			pt1+=1
		elif i==b:
			if pt2%2==0:
				M.append(1)
			else:M.append(3)
			pt2+=1
		else:M.append(1)
	for i in M:print(i,end=' ')
	print()