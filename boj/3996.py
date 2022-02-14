n,k=map(int,input().split())
res=[]
while n:
    res.append(n%k)
    n//=k
res.reverse()
L=[]
if len(res)%2:
    for i in range(len(res)):
        if i%2==0:L.append(res[i])
        else:
            if res[i]==0:continue
            else:break
    L=L+[k-1]*(len(res)//2+1-len(L))
else:
    L=[k-1]*(len(res)//2)
ans=0
# print(res)
# print(L)
for i in L:
    ans*=k
    ans+=i
print(ans+1)