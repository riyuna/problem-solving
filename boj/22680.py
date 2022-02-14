def solve(n):
    x=0
    y=0
    z=0
    mi=n
    for i in range(101):
        if i**3<=n:z=i
        else:break
        nn=n-z**3
        y=int(nn**0.5)
        x=nn-y**2
        mi=min(mi, x+y+z)
    return mi

while True:
    n=int(input())
    if not n:break
    print(solve(n))