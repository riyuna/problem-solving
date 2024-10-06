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
from itertools import permutations
n,k=linput()
L=list(input().strip())
mem=dict()
for i in L:
    if i not in mem:mem[i]=0
    mem[i]+=1
pos=0
for i in mem:pos+=(mem[i]//2)*2
pos+=1
def check(tup, k):
    for i in range(len(tup)-k+1):
        flag=True
        for j in range(k//2):
            if tup[i+j]!=tup[i+k-1-j]:
                flag=False
                break
        if flag:return False
    return True
ct=0
d=dict()
if pos<k:
    res=1
    for i in range(1, n+1):res*=i
    for i in mem:
        for j in range(1, mem[i]+1):res//=j
    print(res)
else:
	for i in permutations(L):
		if i in d:continue
		d[i]=True
		ct+=check(i, k)
	print(ct)
