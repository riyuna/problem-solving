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

import sys
from collections import deque
from itertools import combinations_with_replacement as comb_h
input = sys.stdin.readline
    

p=mod

def fft(L, p, inv=False):
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

def mul(L1, L2, p):
    n=2
    while n<max(len(L1), len(L2)):n*=2
    n*=2
    L1+=[0]*(n-len(L1))
    L2+=[0]*(n-len(L2))
    fft(L1, p)
    fft(L2, p)
    res = [(i*j)%p for i,j in zip(L1, L2)]
    fft(res,p,inv=True)
    return res

n=iinput()
res=[1]
q=deque()
q.append(res)
for i in range(n-1):
    L=[i*2+2, 1]
    fft(L, p)
    print(L)
    q.append(L)
while len(q)>1:
    a=q.popleft()
    b=q.popleft()
    nown=2
    while nown<max(len(a), len(b)):nown*=2
    nown*=2
    a+=[0]*(nown-len(a))
    b+=[0]*(nown-len(b))
    q.append([(i*j)%p for i,j in zip(a,b)])
res=fft(q[0],p,inv=True)
fc=1
for i in range(1, n+1):
    fc*=i
    fc%=mod
print(n)
for i in range(1, n+1):
    print(i,(q[0][i-1]*fc)%mod)