def solve(n ,k):
    if k>=n:k=n-1
    return 4*n*(k+1)-2*k*(k+1)
for i in ' '*int(input()):
    n,k=map(int,input().split())
    print(solve(n,k))