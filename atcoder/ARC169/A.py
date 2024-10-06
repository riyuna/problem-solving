import sys
input = sys.stdin.readline
def linput():return list(map(int,input().split()))

n=int(input())
A=linput()
L=linput()
adj=[[]for i in range(n)]
for i in range(n-1):
	adj[L[i]-1].append(i+1)
d=dict()
d[0]=[0]
visited=[False]*n
visited[0]=True
ct=1
while True:
	d[ct]=[]
	for i in d[ct-1]:
		for j in adj[i]:
			if not visited[j]:
				d[ct].append(j)
	if len(d[ct])==0:break
	ct+=1
res=0
while ct>-1:
	tot=0
	for i in d[ct]:
		tot+=A[i]
	if tot>0:
		res=1
		break
	if tot<0:
		res=-1
		break
	ct-=1
if res>0:print('+')
elif res<0:print('-')
else:print(0)