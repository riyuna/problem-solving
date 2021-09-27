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

def multiply(L):
    if len(L)==1:return L[0]
    if len(L)==2:return mul(L[0],L[1])
    else:
        mid=len(L)//2
        L1=L[:mid]
        L2=L[mid:]
        return mul(multiply(L1),multiply(L2))
    
n=int(input())
L=list(map(int,input().split()))
mulL=[]
for i in L:mulL.append([1,i])
res=multiply(mulL)

for i in ' '*int(input()):
    print(res[int(input())]%100003)