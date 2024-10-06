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

n=iinput()
L=linput()
op=linput()

def ops(L):
    res=[]
    if sum(L)==0:return ['']
    for i in range(4):
        if L[i]!=0:
            L1=L[:]
            L1[i]-=1
            for j in ops(L1):
                res.append('+-*/'[i]+j)
    return res
mn=10**10
mx=-10**10
for i in ops(op):
    now=[]
    for j in range(n):
        now.append(str(L[j]))
        if j!=n-1:
            now.append(i[j])
            if i[j]=='/':now.append('/')
    a=eval(''.join(now))
    mn=min(a,mn)
    mx=max(a,mx)
print(mx)
print(mn)