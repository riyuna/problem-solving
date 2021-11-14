n=int(input())
L=[10**9]*(n+1)
L[0]=0
for i in range(1, n+1):
    if i>1:L[i]=min(L[i-2]+1, L[i])
    if i>4:L[i]=min(L[i-5]+1, L[i])
print(L[n] if L[n]!=10**9 else -1)