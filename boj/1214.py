d,p,q=map(int,input().split())
if p>q:p,q=q,p
res=10**30
if d%p==0 or d%q==0:res=d
# elif (p-1)*(q-1)<d:res=d
else:
    mx=d//q+1
    res=q*mx
    for i in range(mx-1, -1, -1):
        quo=(d-i*q)//p
        r=(d-i*q)%p
        if r==0:
            res=d
            break
        m=(i*q)+(quo+1)*p
        if res==m:break
        else:res=min(res,m)

print(res)