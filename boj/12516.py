t=1
for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	ct=0
	for j in range(1, n+1):
		if j!=L[j-1]:ct+=1
	
	print(f"Case #{t}: {ct}.000000")
	t+=1