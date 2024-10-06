import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
p=998244353
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

n=int(input())
L=list(map(int,input().split()))
d=min(L)

def solve(L):
	if len(L)==1:
		return [1, p-pow(L[0], p-2, p)]
	if len(L)==2:
		a = [1, p-pow(L[0], p-2, p)]
		b = [1, p-pow(L[1], p-2, p)]
		return mul(a, b)
	else:
		L1 = L[:len(L)//2]
		L2 = L[len(L)//2:]
		return mul(solve(L1), solve(L2))
M=solve(L)
res=0
for i in range(n+1):
	res += (M[i]*pow(d, i+1, p)*pow(i+1, p-2, p))%p
	res%= p
print(res)