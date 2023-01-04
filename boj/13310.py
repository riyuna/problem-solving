from functools import cmp_to_key
from collections import deque
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
    if tp1[1]*tp2[0] != tp1[0]*tp2[1]: return cmp(tp1[1]*tp2[0], tp1[0]*tp2[1])
    if tp1[1]!=tp2[1]: return cmp(tp1[1],tp2[1])
    return cmp(tp1[0],tp2[0])

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

for i in ' '*n:
    L.append(list(map(int,input().split())))

stack=deque([])
    
def calipers(stack, L):
    pt1=0
    pt2=1
    first=L[stack[pt1]]
    second=L[stack[pt2]]
    res=(first[0]-second[0])**2+(first[1]-second[1])**2

    for i in range(len(stack)*2):
        npt1=(pt1+1)%len(stack)
        npt2=(pt2+1)%len(stack)
        k1 = (L[stack[npt1]][0]-L[stack[pt1]][0], L[stack[npt1]][1]-L[stack[pt1]][1])
        k2 = (L[stack[pt2]][0]-L[stack[npt2]][0], L[stack[pt2]][1]-L[stack[npt2]][1])
        tmp = k1[0]*k2[1]-k2[0]*k1[1]
        if tmp>0:
            pt1=npt1
        if tmp<0:
            pt2=npt2
        if tmp==0:
            pt1, pt2=npt1, npt2
        
        
        dist=(L[stack[pt1]][0]-L[stack[pt2]][0])**2+(L[stack[pt1]][1]-L[stack[pt2]][1])**2
        if dist>res:
            res=dist
            first=L[stack[pt1]]
            second=L[stack[pt2]]

    return (res, first, second)

def f(L):

	L.sort(key=cmp_to_key(cmp1))
	stdx, stdy=L[0]
	for i in range(n):
		L[i][0]-=stdx
		L[i][1]-=stdy

	L.sort(key=cmp_to_key(cmp2))


	stack.append(0)
	stack.append(1)
	pt=2
	while pt<n:
		while len(stack)>=2:
			first=stack.pop()
			second=stack[-1]
			if ccw(L[second][0], L[second][1], L[first][0], L[first][1], L[pt][0], L[pt][1])>0:
				stack.append(first)
				break
		stack.append(pt)
		pt+=1

	return calipers(stack, L)[0]

