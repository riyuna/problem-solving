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
s=input().strip()

def solve(s):
    if 'O' not in s: return '-'*len(s)
    if 'X' not in s: return '+'*len(s)
    n=len(s)
    ct=0
    L=[]
    for i in s:
        if i=='O' and ct:
            L.append(ct)
            ct=0
        if i=='X':ct+=1
    if s[0]=='X':L[0]+=ct
    else:
        if ct:L.append(ct)
    for i in L:
        if i%2==0:return False
    res=[None]*len(s)
    now=0
    ct=0
    for i in range(len(s)*2):
        i%=n
        if s[i]=='O' and ct:
            ct=0
            now+=1
        if s[i]=='O':res[i]='+'
        if s[i]=='X':
            ct+=1
            if now:
                if ct*2<L[now%len(L)]:res[i]='+'
                else:res[i]='-'
        if now>n:break
    return ''.join(res)

res=solve(s)
if not res:print('NO')
else:
    print('YES')
    print(res)       