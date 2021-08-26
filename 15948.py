n,m=map(int,input().split())
L=list(map(int,input().split()))
sol=[0]*m

def solve(n,m,start=0):
    if m==1:
        sol[start]=L[start]*n
        return
    if n%2:
        sol[start]=L[start]*n
        solve((n+1)//2, m-1, start+1)
        return
    solve(n//2,m-1,start)
    sol[m+start-1] = (n+2**m-2)*L[m+start-1]

solve(n,m)
for i in sol:print(i,end=' ')