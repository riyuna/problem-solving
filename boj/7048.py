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

n,a,b=linput()
L=deque()
def mul(d1, d2):
    res=dict()
    for i in d1:
        for j in d2:
            if i+j not in res:res[i+j]=0
            res[i+j]+=(d1[i])*(d2[j])
            res[i+j]%=2004
    return res
for i in ' '*n:
    k=iinput()
    d=dict()
    d[0]=1
    d[k+1]=-1
    L.append(d)

while len(L)>1:
    p1=L.popleft()
    p2=L.popleft()
    L.append(mul(p1, p2))
    
p=2004

fact=[1,1]
for i in range(2, p):
    fact.append((fact[-1]*i)%p)


def comb(n, k):
    if n<k or n<0:return 0
    if n==0 or k==0:return 1
    if n==k:return 1
    res=1
    for i in range(k):
        res*=(n-i)
    for i in range(k):
        res//=(i+1)
    return res
res=0
for i in L[0]:
    res+=(comb(n+b-i, n)-comb(n+a-i-1, n))*L[0][i]
    res%=p

print(res)