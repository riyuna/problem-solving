n=int(input())
L=list(map(int,input().split()))
mod=10**9+7
res=1
mx=L[0]
mx_pos=0
for i in range(1, n):
    if L[i]>mx:
        mx=L[i]
        res*=(i-mx_pos+1)
        res%=mod
        mx_pos=i
print(res)