from collections import deque
import sys
input = sys.stdin.readline

N , K, M = map(int,input().split())
distance = [0 for _ in range(N+M+1)]
graph = [[] for _ in range(N+M+1)]
for j in range(M):
    L = list(map(int,input().split()))
    for i in L:
        graph[j+N+1].append(i)
        graph[i].append(j+N+1)

que = deque()

def bfs(start):
    que.append(start)
    distance[start] = 1
    while que:
        x = que.popleft()
        if x == N:
            print(distance[x])
            return
        for nx in graph[x]:
            if not distance[nx]:
                if nx >= N+1:
                    distance[nx] = distance[x]
                    que.append(nx)
                else:
                    distance[nx] = distance[x] + 1
                    que.append(nx)
    print(-1)

bfs(1)