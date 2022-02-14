import sys
input=sys.stdin.readline

for i in ' '*int(input()):
    n=int(input())
    s1=input().strip()
    s2=input().strip()
    k1=s1.count('1')
    k2=s2.count('1')
    if k1!=k2 and k1+k2!=(n+1):
        print(-1)
        continue
    res=10**9
    if k1==k2:
        ct=0
        for i in range(n):
            if s1[i]!=s2[i]:ct+=1
        res=min(res, ct)
    if k1+k2==n+1:
        ct=0
        for i in range(n):
            if s1[i]==s2[i]:ct+=1
        res=min(res,ct)
    print(res)