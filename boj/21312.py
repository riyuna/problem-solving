a,b,c=map(int,input().split())
if a%2 or b%2 or c%2:
    res=1
    if a%2:res*=a
    if b%2:res*=b
    if c%2:res*=c
    print(res)
else:print(a*b*c)