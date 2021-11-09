from math import gcd
def solve(k,c):
    flag1=k//abs(k)
    flag2=c//abs(c)
    k=abs(k)
    c=abs(c)
    tmpk=k
    tmpc=c
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
    return ((t1*tmpc-1)//tmpk*flag1, t1*flag2)

def minimizer(a,b,a1,b1):
    mi=abs(a1)+abs(b1)
    mi1=abs(a1+b)+abs(b1-a)
    mi2=abs(a1-b)+abs(b1+a)
    if mi1<mi:
        c=mi
        permc=mi1
        a1+=b
        b1-=a
        while permc<c:
            c=permc
            permc=abs(a1+b)+abs(b1-a)
            if permc>=c:break
            a1+=b
            b1-=a
        if a1*b1==0:return (a1-b,b1+a)
        return (a1,b1)
    elif mi2<mi:
        c=mi
        permc=mi2
        a1-=b
        b1+=a
        while permc<c:
            c=permc
            permc=abs(a1-b)+abs(b1-a)
            if permc>=c:break
            a1-=b
            b1+=a
        if a1*b1==0:return(a1+b, b1-a)
        return (a1,b1)
    else:
        if a1*b1==0:return(a1+b,b1-a)
        return(a1,b1)
for i in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    res=[]
    if n%2==0:
        for i in range(n//2):
            a,b=L[i*2],L[i*2+1]
            res.append(-b//gcd(a,b))
            res.append(a//gcd(a,b))
    else:
        for i in range(n//2-1):
            a,b=L[i*2],L[i*2+1]
            res.append(-b//gcd(a,b))
            res.append(a//gcd(a,b))
        a,b,c=L[-3],L[-2],L[-1]
        g=gcd(a,b)
        a//=g
        b//=g
        a1, b1=solve(a,b)
        b1*=-1
        while a1*b1==0:
            a1-=b
            b1+=a
        a1*=c
        b1*=c
        a1,b1=minimizer(a,b,a1,b1)
        res.append(a1)
        res.append(b1)
        res.append(g)
    for i in res:print(i,end=' ')
    print()