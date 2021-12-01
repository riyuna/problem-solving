import sys
input=sys.stdin.readline
def solve(a,b,x):
    if a>b:a,b=b,a
    if x in (a,b):return True
    while True:
        if a==0:return False
        r=b%a
        if a<x<b:
            if (b-x)%a==0:return True
            return False
        a,b=r,a
        if r==x:return True

for i in ' '*int(input()):
    a,b,x=map(int,input().split())
    print(['NO', 'YES'][solve(a,b,x)])