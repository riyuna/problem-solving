for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	d=dict()
	for i in L:d[i]=True
	n=int(input())
	L=list(map(int,input().split()))
	for i in L:
		print(1 if i in d else 0)