import sys
input=sys.stdin.readline

for i in ' '*int(input()):
    l,r=map(int,input().split())
    mx=0
    c=1
    while c<=r:
        k1=(l-1)//(2*c)*c+max(0, (l-1)%(2*c)-(c-1))
        k2=r//(2*c)*c+max(0, r%(2*c)-(c-1))
        mx=max(k2-k1, mx)
        c*=2
    print(r-l+1-mx)