import sys
input=sys.stdin.readline
for i in ' '*int(input()):
    x,p=map(int,input().split())
    x2,p2=map(int,input().split())
    swapped=False
    if p>p2: 
        swapped=True
        x,p,x2,p2=x2,p2,x,p
    p2-=p
    p=0
    x2big=False
    while p2:
        x2*=10
        p2-=1
        if x2>x:
            x2big=True
            break
    
    if x==x2:
        print('=')
        continue
    if x<x2:x2big=True
    if (x2big and swapped) or (not x2big and not swapped):
        print('>')
    else:print('<')