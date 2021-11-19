def solve(n1, m1, n2, m2):
    res=1
    for i in range(m1+m2):
        res *= (1+i)
    for i in range(n1+n2-m1-m2):
        res *= (1+i)
    for i in range(n1):
        res *= (1+i)
    for i in range(n2):
        res *= (1+i)
    for i in range(m1):
        res /= (1+i)
    for i in range(m2):
        res /= (1+i)
    for i in range(n1-m1):
        res /= (1+i)
    for i in range(n2-m2):
        res /= (1+i)
    for i in range(n1+n2):
        res /= (1+i)
    return res

for i in ' '*int(input()):
    n1,m1,n2,m2=map(int,input().split())
    print(solve(n1,m1,n2,m2))