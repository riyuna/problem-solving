from collections import deque
import sys
input = sys.stdin.readline

N , K, M = map(int,input().split())
visited = [False for _ in range(N+M+1)]
graph = [[] for _ in range(N+M+1)]
for j in range(M):
    L = list(map(int,input().split()))
    for i in L:
        graph[j+N+1].append(i)
        graph[i].append(j+N+1)

que = deque([])

def bfs(start):
    que.append((start,1))
    while que:
        x, count = que.popleft()
        if x == N:
            return (count+1)//2
        if visited[x] == False:
            for i in graph[x]:
                que.append((i,count+1))
            visited[x] == True
    return -1

print(bfs(1))