from decimal import *
def bin_search(l, h, a,b,c,d):
    f=lambda a,b,c,d,x:a*x*x*x+b*x*x+c*x+d
    if f(a,b,c,d,l)*f(a,b,c,d,h)>0:return None
    m=(l+h)/Decimal(2)
    while (h-l)>Decimal(10)**Decimal(-10):
        ll = f(a,b,c,d,l)
        hh = f(a,b,c,d,h)
        m = (l+h)/Decimal(2)
        mm = f(a,b,c,d,m)
        if ll*mm>0:l=m
        else:h=m
    return m

def solve(a,b,c,d):
    dd=b**Decimal(2)-Decimal(3)*a*c
    if dd<0:
        return [bin_search(Decimal(-1000000), Decimal(1000000), a,b,c,d)]
    else:
        x1 = (-b+(dd)**Decimal(0.5))/(Decimal(3)*a)
        x2 = (-b-(dd)**Decimal(0.5))/(Decimal(3)*a)
        if x1>x2:x1,x2=x2,x1
        L=[bin_search(-1000000,x1,a,b,c,d), bin_search(x1,x2,a,b,c,d), bin_search(x2,1000000,a,b,c,d)]
        M=[]
        for i in L:
            if i!= None: M.append(i)
        M.sort()
        res = []
        for i in M:
            if len(res)==0:res.append(i)
            else:
                if i-res[-1]>10**(-9):res.append(i)
        return res

for i in ' '*int(input()):
    a,b,c,d=map(Decimal, input().split())
    L=solve(a,b,c,d)
    for i in L:
        s='%.10f'%i
        if s=='-0.0000000000':s=0
        print(s,end=' ')
    print()