a,b,s=map(int,input().split())
from math import gcd
def solve(k,c):
    tmpk=k
    t1=0
    t2=1
    while c:
        q=k//c
        r=k%c
        t=t1-q*t2
        k=c
        c=r
        t1=t2
        t2=t
    while t1<0:t1+=tmpk
    return t1

g=gcd(a,b)

if a*b==0:
    if a==b:
        if s==0:print('YES')
        else:print('NO')
    else:
        if s%(a+b)==0:print('YES')
        else:print('NO')
elif s%g!=0:print('NO')
else:
    a//=g
    b//=g
    s//=g
    y=solve(a,b)
    x=(1-b*y)//a
    x*=s
    y*=s
    if y<0:print('NO')
    elif x*y==0 and x+y>0:print('YES')
    else:
        k=abs(x)
        c=k//b
        if k%b!=0:c+=1
        x+=c*b
        y-=c*a
        while (gcd(x,y)!=1 and y>=0):
            x+=b
            y-=a
        if y<0:print('NO')
        else:print('YES')