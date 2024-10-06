from functools import cmp_to_key
import sys
input=sys.stdin.readline
n=int(input())
L=[]

def cmp(a, b):
    return (a > b) - (a < b) 

def cmp1(tp1, tp2):
    if tp1[1]!=tp2[1]:return cmp(tp1[1],tp2[1])
    return cmp(tp1[0],tp2[0])

def cmp2(tp1, tp2):
    if tp1[0]==tp1[1]==0:return cmp(0,1)
    if tp2[0]==tp2[1]==0:return cmp(1,0)
    if tp1[1]*tp2[0] != tp1[0]*tp2[1]: return cmp(tp1[1]*tp2[0], tp1[0]*tp2[1])
    if tp1[1]!=tp2[1]: return cmp(tp1[1],tp2[1])
    return cmp(tp1[0],tp2[0])

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

res=0

for i in ' '*n:
    L.append(list(map(int,input().split())))

origL=L[:]
for i in range(n):
	stdx, stdy=origL[i]
	for j in range(n):
		L[j][0]-=stdx
		L[j][1]-=stdy

	L.sort(key=cmp_to_key(cmp2))

	k=1
	t=0

	for j in range(1, n):
		while L[k][0]*L[j][1]-L[j][0]*L[k][1]<=0 and t<n-1:

			t+=1
			k+=1
			if k==n:k=1
		res+=(t-1)*(t-2)//2
	t-=1

	for j in range(n):
		L[j][0]+=stdx
		L[j][1]+=stdy
res//=(n-1)
a=n*(n-1)*(n-2)*(n-3)//24
res-=2*a

b=n*(n-1)*(n-2)//6
print(res/b+3)