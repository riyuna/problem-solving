import sys
input=sys.stdin.readline
def check(n):
    k=(n*2)**0.5
    k=int(k)
    if k*(k+1)//2==n:return True
    return False

for i in ' '*int(input()):
    d=dict()
    def ask(n):
        if n not in d:
            print(f'? 1 {n}')
            sys.stdout.flush()
            k=int(input())
            d[n]=k
            return k
        else:return d[n]
    n=int(input())
    lo=0
    hi=n-1
    while True:
        mid=(lo+hi)//2
        k=ask(mid+1)
        if not check(k):
            hi=mid
        else:
            if k==0:
                lo=mid+1
                continue
            k2=ask(mid)
            if k2==k:
                k3=ask(mid+2)
                if k3==k2+1:
                    j=mid
                    break
                else:hi=mid
            elif check(k2):
                lo=mid+1
            else:
                hi=mid
    j+=1
    k1=ask(j)
    k2=ask(n)-k1
    kk1=int((k1*2)**0.5)
    kk2=int((k2*2)**0.5)
    i=j-kk1-1
    k=j+kk2
    print(f'! {i} {j} {k}')
    sys.stdout.flush()