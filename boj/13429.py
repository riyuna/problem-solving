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
mod=10**9+7

d=iinput()
L=linput()
fact=[1,1]
for i in range(2, 2000010):
    fact.append(fact[-1]*i)
    fact[-1]%=mod
def comb(n, k):
    return (fact[n]*pow(fact[k],mod-2,mod)*pow(fact[n-k],mod-2,mod))%mod
for i in ' '*iinput():
    v,n = linput()
    res=0
    for i in range(d//v+1):
        res+=comb(n-1+i, i)*L[d-v*i]*((-1)**(i))
        # print(comb(n-1+i, i), L[d-v*i])
        res%=mod
    print(res)