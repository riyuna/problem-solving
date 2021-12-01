from functools import cmp_to_key
from collections import deque
import sys
input=sys.stdin.readline

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

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    return ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<0

def onLine(pt1, pt2, pt3):
    #pt1, pt2로  이루어진 선분 위에 pt3이 있는가
    if not ((pt1[0]<=pt3[0]<=pt2[0]) and (pt1[1]<=pt3[1]<=pt2[1])):return False
    return pt1[0]*pt2[1]+pt2[0]*pt3[1]+pt3[0]*pt1[1] == pt1[0]*pt3[1]+pt3[0]*pt2[1]+pt2[0]*pt1[1]

def inConvex(stack, L, ptx, pty):
    isplus=False
    isminus=False
    online=False
    for i in range(len(stack)):
        first, second=L[stack[i-1]], L[stack[i]]
        k=ccw(second[0],second[1],first[0],first[1],ptx,pty)
        if k>0:isplus=True
        if k<0:isminus=True
        if k==0 and onLine(first, second, [ptx, pty]):online=True
    
    if isplus and isminus and not online:return False
    return True
    

for _ in ' '*int(input()):
    n,m=map(int,input().split())
    L1=[]

    for i in ' '*n:
        L1.append(list(map(int,input().split())))

    L1.sort(key=cmp_to_key(cmp1))
    stdx, stdy=L1[0]
    for i in range(n):
        L1[i][0]-=stdx
        L1[i][1]-=stdy

    L1.sort(key=cmp_to_key(cmp2))
    # print(L)

    stack1=deque([])
    stack1.append(0)
    stack1.append(1)
    pt=2
    while pt<n:
        while len(stack1)>=2:
            first=stack1.pop()
            second=stack1[-1]
            if ccw(L1[second][0], L1[second][1], L1[first][0], L1[first][1], L1[pt][0], L1[pt][1])>0:
                stack1.append(first)
                break
        stack1.append(pt)
        pt+=1
    if n==1:stack1.pop()

    for i in range(len(L1)):
        L1[i][0]+=stdx
        L1[i][1]+=stdy

    L2=[]

    for i in ' '*m:
        L2.append(list(map(int,input().split())))

    L2.sort(key=cmp_to_key(cmp1))
    stdx, stdy=L2[0]
    for i in range(m):
        L2[i][0]-=stdx
        L2[i][1]-=stdy

    L2.sort(key=cmp_to_key(cmp2))
    # print(L)

    stack2=deque([])
    stack2.append(0)
    stack2.append(1)
    pt=2
    while pt<m:
        while len(stack2)>=2:
            first=stack2.pop()
            second=stack2[-1]
            if ccw(L2[second][0], L2[second][1], L2[first][0], L2[first][1], L2[pt][0], L2[pt][1])>0:
                stack2.append(first)
                break
        stack2.append(pt)
        pt+=1
    if m==1:stack2.pop()

    for i in range(len(L2)):
        L2[i][0]+=stdx
        L2[i][1]+=stdy

    state=True
    if len(stack2)>2:
        for i in stack1:
            if inConvex(stack2, L2, L1[i][0], L1[i][1]):
                state=False
                break
    
    elif len(L2)==2:
        first=L2[stack2[0]]
        second=L2[stack2[1]]
        for i in stack1:
            if onLine(first, second, L1[i]):
                state=False
                break
    
    if len(stack1)>2:
        for i in stack2:
            if inConvex(stack1, L1, L2[i][0], L2[i][1]):
                state=False
                break

    elif len(L1)==2: 
        first=L1[stack1[0]]
        second=L1[stack1[1]]
        for i in stack2:
            if onLine(first, second, L2[i]):
                state=False
                break
    
    if len(L1)==len(L2)==2:
        if cross(L1[0][0], L1[0][1], L1[1][0], L1[1][1], L2[0][0], L2[0][1], L2[1][0], L2[1][1]):
            state=False
    
    print(['NO', 'YES'][state])