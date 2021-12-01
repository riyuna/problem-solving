def solve(a,b):
    if (a+b)%2:return (-1, -1)
    if a%2:
        return (a//2)+1, b//2
    return a//2, b//2
for i in ' '*int(input()):
    a,b=map(int,input().split())
    c,d=solve(a,b)
    print(c,d)