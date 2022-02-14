import heapq
import sys
from math import ceil
input=sys.stdin.readline

def calc(c, tax):
	return c-ceil(c*tax/100)

v,e=map(int,input().split())
s,t,candy=map(int,input().split())
L=[[]for i in range(v)]
for i in ' '*e:
	a,b,c=map(int,sys.stdin.readline().split())
	L[a-1].append((b,c))
	L[b-1].append((a,c))
dist=[]
distm=[-1]*v
distm[s-1]=candy
heapq.heappush(dist,(0,s))
while True:
	if len(dist)==0:break
	a=heapq.heappop(dist)
	if -a[0]>distm[a[1]-1]:continue
	else:
		for i in L[a[1]-1]:
			res=calc(distm[a[1]-1],i[1])
			if res>distm[i[0]-1]:
				distm[i[0]-1]=res
				heapq.heappush(dist,(-res,i[0]))

print(distm[t-1])