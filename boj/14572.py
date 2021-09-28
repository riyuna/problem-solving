import sys
input=sys.stdin.readline
n,K,d=map(int,input().split())
L=[]
for i in ' '*n:
    m,sc=map(int,input().split())
    al=0
    for k in list(map(int,input().split())):
        k-=1
        al|=1<<k
    L.append([sc,al])

L.sort()
cnt=[0]*31
l=0
r=0
ans=0
while r<n:
    while L[r][0]-L[l][0]>d:
        for i in range(K):
            if L[l][1]&(1<<i): cnt[i]-=1
        l+=1
    for i in range(K):
        if L[r][1]&(1<<i): cnt[i]+=1
    score=0
    for i in range(K):
        if 0<cnt[i]<r-l+1: score+=1
    ans = max(ans, score*(r-l+1))

    r+=1

print(ans)