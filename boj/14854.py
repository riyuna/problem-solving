import sys
input=sys.stdin.readline

dp=[[-1]*2010 for i in range(2010)]
def c(x,y,m):
    if x<y:
        dp[x][y]=0
        return 0
    if y==0 or y==x:
        dp[x][y]=1
        return 1
    if dp[x][y]!=-1:return dp[x][y]
    k=(c(x-1,y-1,m)+c(x-1,y,m))%m
    dp[x][y]=k
    return k

def solve_27(n,m):
    r=n-m
    nL=[]
    mL=[]
    rL=[]
    ct=0
    while n or m or r or ct<3:
        nL.append(n%3)
        mL.append(m%3)
        rL.append(m%3)
        n//=3
        m//=3
        r//=3
        ct+=1
    