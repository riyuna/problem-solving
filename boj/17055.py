# n,k=map(int,input().split())
# L1=list(map(int,input().split()))
# L2=list(map(int,input().split()))
with open("contest6_testdata/simfonija/simfonija.in.2a") as f:
    n,k=map(int,f.readline().split())
    L1=list(map(int,f.readline().split()))
    L2=list(map(int,f.readline().split()))
L=[]
for i in range(n):L.append(L2[i]-L1[i])
L.sort()

sL=[0]
ans=10**9
if n==k or n==k+1:ans=0
for i in L:sL.append(sL[-1]+i)

# print(L)
# print(sL)

if ans:
    for i in range(k+1):
        print(L[i:i+n-k])
        mid=i+(n-k)//2
        res=abs(sL[mid+1]-sL[i]-L[mid]*(mid-i+1))+abs(sL[i+n-k]-sL[mid]-L[mid]*(i+n-k-mid))
        # print(mid-i+1)
        # print(i+n-k-mid)
        print(res)
        ans=min(ans, res)

print(ans)