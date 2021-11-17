import sys
input=sys.stdin.readline
def solve(a,b,c,d):
    if b==c==d==0:
        return a+1
    if c==d==0:
        if a==0:return b+1
        return a+2*b+1
    if d==0:
        if a==0:
            if b==0:return 1+c
            if b==1:return 2+2*c
            return 2*b+3*c-1
        if b==0 and a==1:return 2+2*c
        return a+2*b+3*c+1
    if a==b==c==0:return d+1
    if a==b==0:
        if c<4:return (c+1)*(d+1)
        if d<=2:return (c+1)*(d+1)
        return 3*c+4*d-5
    if a==0:
        if c==0:return solve(b,d,0,0)
        return 4*d+3*c+2*b-1
    if a==1:
        if b>=1:return d*4+c*3+b*2+a+1
        if c==0:return 2*d+2
        if c==1:return 3*d+4
        return 4*d+3*c
    if a==2:
        if b==c==0:return 3*d+3
    return 4*d+3*c+2*b+a+1
for i in ' '*int(input()):
    a,b,c,d=map(int,input().split())
    print(solve(a,b,c,d))