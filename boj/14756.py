import sys
input = sys.stdin.readline
p=469762049

def fft(L, inv=False):
    j=0
    n=len(L)
    for i in range(1, n):
        bit = n>>1
        while j>=bit:
            j-=bit
            bit>>=1
        j+=bit
        if i<j:L[i],L[j]=L[j],L[i]
    m=2
    while m<=n:
        u = pow(3, p//m, p)
        if inv: u=pow(u, p-2, p)
        for i in range(0, n ,m):
            w=1
            for k in range(i, i+m//2):
                tmp=L[k+m//2]*w
                L[k+m//2] = (L[k]-tmp)%p
                L[k] += tmp
                L[k]%=p
                w*=u
                w%=p
        m*=2
    if inv:
        inv_n = p-(p-1)//n
        for i in range(n):
            L[i]=(L[i]*inv_n)%p

def mul(L1, L2):
    n=2
    while n<max(len(L1), len(L2)):n*=2
    n*=2
    L1+=[0]*(n-len(L1))
    L2+=[0]*(n-len(L2))
    fft(L1)
    fft(L2)
    res = [(i*j)%p for i,j in zip(L1, L2)]
    fft(res,inv=True)
    return res

n,l,m,w=map(int,input().split())
L=[]
M=[]
res=[0]*(n-l+1)
for i in ' '*m:L.append(list(map(int,input().split())))
for i in ' '*m:M.append(list(map(int,input().split())))
for i in range(m):
	L1=mul(L[i],M[i][::-1])
	for j in range(l-1, n):
		res[j-l+1]+=L1[j]
		
ct=0
for i in res:
	if i>w:ct+=1
print(ct)