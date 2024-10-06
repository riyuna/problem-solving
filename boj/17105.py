#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from collections import deque
if str(os.getcwd())[:10]==r'C:\Users\r':
    sys.stdin=open('input.txt', 'r')
    sys.stdout=open('output.txt','w')
input=sys.stdin.readline
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353
mod=998244353
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

pL=[True]*1000001
pL[0]=False
pL[1]=False
L1=[0]*1000001
L2=[0]*1000001
for i in range(2, 1001):
    if not pL[i]:continue
    for j in range(i*2, 1000001, i):pL[j]=False

for i in range(2, 1000001):
    if pL[i]:
        L1[i]=1
        if i*2<1000001:L2[i*2]=1
        
res0=mul(L1[:], L1[:])
res1=mul(L1[:], res0)
res2=mul(L1[:], L2[:])

print(res1[:100])
print(res2[:100])