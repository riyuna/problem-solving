import sys
input=sys.stdin.readline
dp=[[0]*5001 for i in range(5001)]
K=[[0]*5001 for i in range(5001)]
def solve(L):
    s=[0]
    for i in L:s.append(s[-1]+i)
    for i in range(1, len(L)+1):
        dp[i-1][i]=0
        K[i-1][i]=i
    
    for i in range(2, len(L)+1):
        for j in range(len(L)-i+1):
            pt=i+j
            dp[j][pt]=10**10
            for k in range(K[j][pt-1], K[j+1][pt]+1):
                rem=dp[j][k]+dp[k][pt]+s[pt]-s[j]
                if rem<dp[j][pt]:
                    dp[j][pt]=rem
                    K[j][pt]=k
    
    return dp[0][len(L)]

for _ in ' '*int(input()):
    n=int(input())
    L=list(map(int,input().split()))
    print(solve(L))