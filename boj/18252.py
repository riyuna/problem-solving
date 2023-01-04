# from functools import cmp_to_key
from collections import deque
import sys
input=sys.stdin.readline

stars = []
L=[]
n=int(input())
y1, x1, y2, x2 = map(int,input().split())
for i in ' '*n:stars.append(tuple(map(int,input().split())))

m = (y2-y1)/(x2-x1)
b = (y1*x2-y2*x1)/(x2-x1)
L.append([x1, y1])
L.append([x2, y2])
for x, yst, yen in stars:
    k = m*x+b
    if yst<=k<=yen:L.append([x, k])
    elif yst>k:L.append([x, yst])
    else:L.append([x, yen])

def cmp(a, b):
    return (a > b) - (a < b) 


def cmp2(tp1, tp2):
    if tp1[1]*tp2[0] != tp1[0]*tp2[1]: return cmp(tp1[1]*tp2[0], tp1[0]*tp2[1])
    if tp1[1]!=tp2[1]: return cmp(tp1[1],tp2[1])
    return cmp(tp1[0],tp2[0])
	
def anglesort(L):
	if len(L)<=1:return L
	piv = L[0]

	l = [i for i in L[1:] if cmp2(piv, i)>0]
	r = [i for i in L[1:] if cmp2(piv, i)<=0]

	return anglesort(l)+[piv]+anglesort(r)

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2+x2*y3+x3*y1) - (y1*x2+y2*x3+y3*x1)

def area(p1, p2, p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3
    return abs(ccw(x1,y1,x2,y2,x3,y3)/2)

minstdx, minstdy = L[0]
n+=2
# for i in range(n):
# 	if L[i][1]<minstdy:
# 		minstdy=L[i][1]
# 		minstdx=L[i][0]

for i in range(n):
    L[i][0]-=minstdx
    L[i][1]-=minstdy

L=[L[0]]+anglesort(L[1:])
# L.sort(key=cmp_to_key(cmp2))
# print(L)

stack=deque([])
stack.append(0)
stack.append(1)
pt=2
while pt<n:
    while len(stack)>=2:
        first=stack[-1]
        second=stack[-2]
        if ccw(L[second][0], L[second][1], L[first][0], L[first][1], L[pt][0], L[pt][1])>0:
            break
        stack.pop()
    stack.append(pt)
    pt+=1


def solve(stack):
    if len(stack)<3:return 0
    n=len(stack)
    a,b,c=0,1,1
    mx = 0
    for a in range(n):
        b=a+1
        c=a+2
        b%=n
        c%=n
        while True:
            if area(L[stack[a]], L[stack[b]], L[stack[c]]) < area(L[stack[a]], L[stack[(b+1)%n]], L[stack[c]]):
                b+=1
                b%=n
            else:
                c+=1
                c%=n
            if area(L[stack[a]], L[stack[b]], L[stack[c]]) > mx:
                mx = area(L[stack[a]], L[stack[b]], L[stack[c]])

            if c==a:break

    if mx<10**-6:return 0
    return mx

def bf(stack):
    res=0
    for i in range(len(stack)):
        for j in range(i+1, len(stack)):
            for k in range(j+1, len(stack)):
                arr1 = area(L[stack[i]], L[stack[j]], L[stack[k]])
                res = max(res, arr1)
    return res if res>10**-6 else 0

if len(stack) in (3, 4, 5):print(bf(stack))
else:print(solve(stack))