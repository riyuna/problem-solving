import heapq
import sys
input=sys.stdin.readline
MAX=1000000000000000000
n,m=map(int,input().split())
L=[[]for i in range(n)]
for i in range(m):
	a,b=map(int,input().split())
	L[a-1].append((b,i+1))
	L[b-1].append((a,i+1))
dist=[]
distm=[MAX]*n
distm[0]=0
heapq.heappush(dist,(0,1))
while True:
	if len(dist)==0:break
	a=heapq.heappop(dist)
	for i in L[a[1]-1]:
		if i[1]>a[0]:
			tm=i[1]
		else:
			tm=i[1]%m+(a[0])//m*m
			if tm<a[0]:tm+=m
		if tm<distm[i[0]-1]:
			distm[i[0]-1]=tm
			heapq.heappush(dist,(tm,i[0]))
print(distm[-1])