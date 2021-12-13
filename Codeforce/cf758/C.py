import sys
input=sys.stdin.readline

for _ in ' '*int(input()):
    n=int(input())
    L1=list(map(int,input().split()))
    L2=list(map(int,input().split()))
    Lpair=[]
    for i in range(n):
        Lpair.append([L1[i], L2[i]])
    Lpair.sort()
    d1=dict()
    mi=10**9+1
    for i in range(n-1, -1, -1):
        mi=min(mi, Lpair[i][1])
        d1[Lpair[i][0]]=mi

    for i in range(n):
        Lpair[i][0], Lpair[i][1]=Lpair[i][1], Lpair[i][0]

    Lpair.sort()
    d2=dict()
    mi=10**9+1
    for i in range(n-1, -1, -1):
        mi=min(mi, Lpair[i][1])
        d2[Lpair[i][0]]=mi
    amin=Lpair[-1][1]
    bmin=10**9+1
    while True:
        bperm=min(d1[amin], bmin)
        aperm=min(d2[bperm], amin)
        if (aperm, bperm)==(amin, bmin):break
        amin,bmin=aperm,bperm
    for i in range(n):
        if L1[i]>=amin or L2[i]>=bmin:print('1',end='')
        else:print('0',end='')
    print()