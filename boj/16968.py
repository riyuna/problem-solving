res=1
last=None
mod=10**9+9
for i in input():
    if i=='d':
        if last=='d':res*=9
        else:res*=10
    else:
        if last=='c':res*=25
        else:res*=26
    last=i
    res%=mod
print(res)