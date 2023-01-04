from datetime import datetime
import time

n=int(input())
dt_format = "%Y/%m/%d %H:%M:%S"
L=[]
dtL=[]

def tot_year(t1, t2):
	return ((t2-t1).total_seconds())/(365*86400)

for i in ' '*n:
	t1, t2,l=input().split()
	t = t1+' '+t2
	l=int(l)
	dt = datetime.strptime(t, dt_format)
	dtL.append(dt)
	L.append(l)

weight = []
for i in range(n):
	weight.append(max(pow(0.5, tot_year(dtL[i],dtL[-1])), pow(0.9, n-i-1)))

res = 0
for i in range(n):res += weight[i]*L[i]

print(round(res/sum(weight))) if weight else print(0)