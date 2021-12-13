n=int(input())
adj=[[]for i in range(n)]
for i in range(n):
    L=list(map(int,input().split()))
    for j in range(n):
        if L[j]:
            adj[i].append(j)

print(adj)
def solve(adj):
    for i in adj:
        if len(i)%2:return False
    