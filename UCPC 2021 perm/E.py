n,k=map(int,input().split())
H = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mi = 10**10

def f(pos, k, x):
    res=0
    for i in range(pos, pos+k):
        if x<H[i]:res+=(H[i]-x)*B[i]
        else: res+=(x-H[i])*A[i]
    return res

for i in range(n-k+1):
    lo = 0
    hi = 10**5
    a = (2*lo+hi)//3
    b = (lo+2*hi)//3
    while (hi-lo)>2:
        a = (2*lo+hi)//3
        b = (lo+2*hi)//3
        aa = f(i,k,a)
        bb = f(i,k,b)
        if aa>bb:
            lo=a
        else: 
            hi=b
    res = (hi+lo)//2
    mi=min(mi, f(i, k, res))
    mi=min(mi, f(i, k, res+1))
    mi=min(mi, f(i, k, res-1))

print(mi)
