#君の手を握ってしまったら
#孤独を知らないこの街には
#もう二度と帰ってくることはできないのでしょう
#君が手を差し伸べた 光で影が生まれる
#歌って聞かせて この話の続き
#連れて行って見たことない星まで
#さユリ - 花の塔                        
import sys, os
from sys import exit
from collections import deque
input=sys.stdin.readline
flush=sys.stdout.flush
def iinput():return int(input())
def linput():return list(map(int,input().split()))
mod=998244353

n=iinput()

L=deque()
for i in range(n):
    L.append([i+1])
while len(L)>1:
    L1=L.popleft()
    L2=L.popleft()
    newL=[]
    ct1=0
    ct2=0
    while ct1<len(L1) and ct2<len(L2):
        print(f"? {L1[ct1]} {L2[ct2]}")
        flush()
        k=iinput()
        if k==-1:exit(1)
        if k==1:
            newL.append(L1[ct1])
            ct1+=1
        else:
            newL.append(L2[ct2])
            ct2+=1
    while ct1<len(L1):
        newL.append(L1[ct1])
        ct1+=1
    while ct2<len(L2):
        newL.append(L2[ct2])
        ct2+=1
    L.append(newL)
order=L[0]
ct=n
while len(order)>1:
    ct+=1
    print(f"+ {order[0]} {order[-1]}")
    flush()
    iinput()
    order.pop(len(order)-1)
    order.pop(0)
    # print(order)
    if len(order):
        lo=0
        hi=len(order)
        mid=(lo+hi)//2
        while lo<hi:
            mid=(lo+hi)//2
            print(f"? {order[mid]} {ct}")
            flush()
            k=iinput()
            if k==-1:exit(0)
            if k==1:
                lo=mid+1
            else:
                hi=mid
            # print(f"lo: {lo}, mid:{mid}, hi:{hi}")
        order.insert(hi, ct)
    else:order.append(ct)
print('!')
exit(0)