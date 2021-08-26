n,m,s=map(int,input().split())
L=list(map(int,input().split()))
inj = [[False]*n for i in range(n)]
for _ in ' '*m:
    u,v,w=map(int,input().split())
    inj[u-1][v-1] = w
    inj[v-1][u-1] = w
    