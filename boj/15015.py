import sys
from bisect import bisect_left
input=sys.stdin.readline
n=int(input())
xh,yh,xw,yw=map(int,input().split())
incx=1
incy=1
if xh>xw:incx=-1
if yh>yw:incy=-1
x0=min(xh,xw)
x1=max(xh,xw)
y0=min(yh,yw)
y1=max(yh,yw)
L=[]
for i in ' '*n:
	x,y=map(int,input().split())
	if x0<=x<=x1 and y0<=y<=y1:
		L.append((x*incx,y*incy))
L.sort()
M=[]
ct=0
for x,y in L:
	M.append(y+ct/len(L))
	ct+=1

def put(L,n):
    k=len(L)-1
    upp=k
    low=0
    if len(L)==0:
        L.append(n)
        return
    if L[upp]<n:
        L.append(n)
        return
    if L[low]>n:
        L[0]=n
        return
    while True:
        if L[upp]==n or L[low]==n:
            return
        if upp==low:
            L[upp]=n
            return
        if upp==low+1:
            L[upp]=n
            return
        else:
            t=L[(upp+low)//2]
            if t<n:low=(upp+low)//2
            else:upp=(upp+low)//2
    return

def solve(L):
	M=[]
	for i in L:
		put(M, i)
	return len(M)

print(solve(M))