n,m=map(int,input().split())
res=''
if n==0:res='0'
while n:
    r=n%m
    n//=m
    s=''
    if r>9:
        s='ABCDEF'[r-10]
    else:s=str(r)
    res=s+res
print(res)