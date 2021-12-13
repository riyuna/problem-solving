import sys
input=sys.stdin.readline

def lattice(a,b,c):
    if a+b>c:return 0
    if a<b:a,b=b,a
    q=a//b
    r=a%b
    t=(q*c+r)//a
    k = (t-1) // q * (2*t-q*(1+(t-1)//q))//2
    return k+lattice(b,r,c-b*t)

for i in ' '*int(input()):
    p,q,n=map(int,input().split())
    res=p*n*(n+1)//2
    print(res-q*lattice(p,q,p*(n+1)))