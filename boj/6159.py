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

n,s=linput()
L=[]
for i in ' '*n:L.append(iinput())
L.sort()
ct=0
pt1=0
pt2=n-1
while pt2>pt1:
    while L[pt1]+L[pt2]>s:
        pt2-=1
    if pt2<=pt1:break
    ct+=(pt2-pt1)
    pt1+=1
print(ct)