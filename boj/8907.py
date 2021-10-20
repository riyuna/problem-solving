import sys
input=sys.stdin.readline
t=int(input())
for _ in ' '*t:
    n=int(input())
    ct=[0]*n
    for i in range(n-1):
        L=list(map(int,input().split()))
        for j in range(len(L)):
            if L[j]:
                ct[i]+=1
                ct[i+j+1]+=1
    res=0
    for i in range(n):
        res+=ct[i]*(n-1-ct[i])
    print(n*(n-1)*(n-2)//6-res//2)