import sys, heapq
input=sys.stdin.readline
n1,n2,m=map(int,input().split())
L=[[]for i in range(n1+n2)]
for i in ' '*m:
	a,b=map(int,input().split())
	L[a-1].append((b,1))
	L[b-1].append((a,1))
def dijks(k):
	dist=[]
	distm=[10**10]*(n1+n2)
	distm[k-1]=0
	heapq.heappush(dist, (0, k))
	while True:
		if len(dist)==0:break
		a=heapq.heappop(dist)
		if a[0]>distm[a[1]-1]:continue
		else:
			for i in L[a[1]-1]:
				if i[1]+distm[a[1]-1]<distm[i[0]-1]:
					distm[i[0]-1]=i[1]+distm[a[1]-1]
					heapq.heappush(dist, (i[1]+distm[a[1]-1], i[0]))
	mem=0
	for i in distm:
		if i!=10**10:mem=max(mem, i)
	return mem
print(dijks(1)+dijks(n1+n2)+1)