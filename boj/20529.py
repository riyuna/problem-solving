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
def dif(s1, s2):
    ct=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:ct+=1
    return ct
for _ in ' '*iinput():
    n=iinput()
    L=input().split()
    if n>32:
        print(0)
        continue
    else:
        res=10**10
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    s1,s2,s3=L[i],L[j],L[k]
                    d=dif(s1,s2)+dif(s2,s3)+dif(s3,s1)
                    res=min(res,d)
        print(res)