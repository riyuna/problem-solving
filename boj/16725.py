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
mod=10**9+9

n,m,k=linput()
res=0
fact=[1,1]
for i in range(2, 1048573):
    fact.append((fact[-1]*i)%mod)

def c(n, k):
    if n<k:return 0
    if k<0:return 0
    if n<0:return 0
    return (fact[n]*pow(fact[k],mod-2,mod)*pow(fact[n-k],mod-2,mod))%mod

def comb(n,k):
    count=1
    while n or k:
        count*=c(n%mod, k%mod)
        count%=mod
        n//=mod
        k//=mod
    return count

for i in range((k//(n+1))+1):
    res+=comb(m ,i)*comb(m+k-n*i-i-1, m-1)*(-1)**i
    res%=mod
print(res)