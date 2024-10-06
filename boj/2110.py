import sys
input = sys.stdin.readline
n,c=map(int,input().split())
L=[]
for i in ' '*n:L.append(int(input()))
L.sort()
mn=1
mx=1000000000
while(mn<=mx):
    mid=(mx+mn)//2
    last=0
    count=0
    for i in range(n):
        if i==0:
            last=L[i]
            count+=1
            continue
        if L[i]>=last+mid:
            last=L[i]
            count+=1
    if count>=c:
        mn=mid+1
        ans=mid
    else:
        mx=mid-1
print(ans)