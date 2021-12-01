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

L.sort(key=cmp_to_key(cmp1))
stdx, stdy=L[0]
for i in range(n):
    L[i][0]-=stdx
    L[i][1]-=stdy

L.sort(key=cmp_to_key(cmp2))
# print(L)

stack=deque([])
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

print(len(stack))