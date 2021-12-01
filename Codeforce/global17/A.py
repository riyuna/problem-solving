import sys
input=sys.stdin.readline
for i in ' '*int(input()):
    a,b=map(int,input().split())
    if a==b==1:print(0)
    elif min(a,b)==1:print(1)
    else:print(2)