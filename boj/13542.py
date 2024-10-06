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

n,m,k,p=linput()

fact=[1,1]
for i in range(2, p):
    fact.append((fact[-1]*i)%p)

def c(n,k):
    if n<k:return 0
    if k==0 or k==n:return 1
    return (fact[n]*pow(fact[k],p-2,p)*pow(fact[n-k],p-2,p))%p

def comb(n,k):
    count=1
    while n or k:
        count*=c(n%p, k%p)
        count%=p
        n//=p
        k//=p
    return count

res=0
for i in range(n+1):
    if (k-i)%2:continue
    res+=comb(n,i)*comb(n+m+(k-i)//2-1, (k-i)//2)
    res%=p
print(res)