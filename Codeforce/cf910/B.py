import sys
input=sys.stdin.readline
for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))[::-1]
	M=[]
	res=0
	for i in L:
		if len(M)==0:
			M.append(i)
			continue
		if M[-1]>=i:
			M.append(i)
			continue
		k=i//M[-1]
		if i%M[-1]:k+=1
		res+=(k-1)
		M.append(i//k)
	print(res)