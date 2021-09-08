n=int(input())
L=list(map(float,input().split()))
res=0
for i in range(n):
    res+=L[i]
for i in range(n-1):
    res+=(L[i]*(1-L[i+1]))
    res+=((1-L[i])*L[i+1])
print(res)