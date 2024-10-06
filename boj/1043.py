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

n,m=linput()
truth=linput()[1:]
p=[-1]*(51)

def find(a):
    if p[a]<0:return a
    p[a]=find(p[a])
    return p[a]
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:return
    p[b]=a
party=[]
for _ in range(m):
    L=linput()[1:]
    party.append(L)
    for i in range(1, len(L)):
        merge(L[i],L[0])
ct=0
for pt in party:
    lie=True
    for i in pt:
        flag=True
        for j in truth:
            if find(i)==find(j):
                flag=False
                break
        if not flag:
            lie=False
            break
    ct+=lie
print(ct)