import heapq

n, m, t, dis = map(int, input().split())
L_repair = list(map(int, input().split()))
L_repair.append(1)
L_repair.append(n)
L_repair.sort()

d = [[0] * (n) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i!=j:d[i][j]=1000000000000000000
for i in ' '*m:
    a,b,c=map(int,input().split())
    d[a-1][b-1]=min(d[a-1][b-1],c)
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if d[i-1][k-1]+d[k-1][j-1]<d[i-1][j-1]:
                d[i-1][j-1]=d[i-1][k-1]+d[k-1][j-1]
for l in d:print(l)
L_new =[[] for i in range(n)]
for i in L_repair:
    for j in L_repair:
        if i == j:
            break
        if d[j-1][i-1] <= dis:
            L_new[i-1].append((j, d[j-1][i-1]))
            L_new[j-1].append((i, d[j-1][i-1]))
print(L_new)

dist=[]
distm=[1000000000000000000]*n
distm[0]=0
heapq.heappush(dist,(0,1))
while True:
    if len(dist)==0:break
    a=heapq.heappop(dist)
    if a[0]>distm[a[1]-1]:continue
    else:
        for i in L_new[a[1]-1]:
            if i[1]+distm[a[1]-1]<distm[i[0]-1]:
                distm[i[0]-1]=i[1]+distm[a[1]-1]
                heapq.heappush(dist,(i[1]+distm[a[1]-1],i[0]))

if distm[n-1]!=1000000000000000000:
    print(distm[n-1])
else:
    print('stuck')