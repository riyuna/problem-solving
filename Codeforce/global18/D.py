import sys
input=sys.stdin.readline
print=sys.stdout.write
    
for i in ' '*int(input()):
    rem=dict()
    n,m=map(int,input().split())
    p=[-1]*(2*n+1)
    def find(a):
        if p[a]<0:return a
        p[a]=find(p[a])
        return p[a]
    def merge(a,b):
        a=find(a)
        b=find(b)
        if a==b:return
        p[b]=a
    
    def same(a,b):
        a=find(a)
        b=find(b)
        return a==b
    
    molu=[]
    for i in ' '*(n-1):
        x,y,v=map(int,input().split())
        if v==-1:molu.append((x,y))
        else:
            ct=0
            vv=v
            while v:
                ct+=(v%2)
                v//=2
            if ct%2:
                merge(x,y+n)
                merge(y,x+n)
            else:
                merge(x,y)
                merge(x+n,y+n)
            rem[(x,y)]=vv
    
    for i in ' '*m:
        x,y,v=map(int,input().split())
        ct=0
        if v:
            merge(x,y+n)
            merge(y,x+n)
        else:
            merge(x,y)
            merge(x+n,y+n)
    
    res=True
    for i in range(1, n+1):
        if same(i, i+n):
            res=False
            break
    if not res:print('NO\n')
    else:
        print('YES\n')
        for a,b in molu:
            if same(a,b):
                print(f'{a} {b} 0\n')
            elif same(a,b+n):
                print(f'{a} {b} 1\n')
            else:
                print(f'{a} {b} 0\n')
                merge(a,b)
                merge(a+n,b+n)
        for a,b in rem:
            print(f'{a} {b} {rem[(a,b)]}\n')