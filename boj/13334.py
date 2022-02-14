import sys
import heapq

input=sys.stdin.readline
n=int(input())
L=[]
for i in ' '*n:
	a,b=map(int,input().split())
	if a>b:a,b=b,a
	L.append((a,b))
ln=int(input())
L.sort(key=lambda x:(x[1],x[0]))

q=[]
res=0
pt=0
while pt<n:
	a,b=L[pt]
	if a+ln<b:
		pt+=1
		continue
	heapq.heappush(q, a)
	while q[0]+ln<b:
		heapq.heappop(q)
	res=max(res, len(q))
	pt+=1
print(res)