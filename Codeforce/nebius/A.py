import sys
input=sys.stdin.readline
for i in ' '*int(input()):
    a,b=map(int,input().split())
    a=abs(a)
    b=abs(b)
    k=max(a,b)
    if a==b:print(k*2)
    else:print(k*2-1)