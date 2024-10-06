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

n,k=linput()
L1=linput()
L2=linput()
adj=[]
for i in range(n):
    adj.append(L1[i]-1)


def adjpow(L, n):
    if n==0:return list(range(len(L)))
    if n==1:return L[:]
    L1=adjpow(L, n//2)
    res=[]
    for i in range(len(L1)):
        res.append(L1[L1[i]])
    if n%2:
        newres=[]
        for i in range(len(L1)):
            newres.append(res[L[i]])
        res=newres
    return res

for i in adjpow(adj, k):
    print(L2[i],end=' ')
print()