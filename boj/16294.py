import sys
import heapq


input = sys.stdin.readline


def search(i, j):
	global visited, n, m

	stk = [(i, j)]
	cnt = 0

	while stk:
		i, j = stk.pop()

		if visited[i][j]:
			continue

		visited[i][j] = True
		cnt += 1

		if i%2:
			next = [(i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j), (i+1, j+1)]
		else:
			next = [(i-1, j-1), (i-1, j), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j)]
		
		for ni, nj in next:
			if ni < 0 or nj < 0 or ni >= n or nj >= m:
				continue
			if visited[ni][nj]:
				continue
			if field[ni][nj] != 0:
				continue
			stk.append((ni, nj))
	
	return cnt


if __name__ == "__main__":
	h, n, m = map(int, input().split())

	field = [[-1 for _ in range(m)] for _ in range(n)]
	visited = [[False for _ in range(m)] for _ in range(n)]

	for i in range(n):
		line = input().split()

		for j in range(m):
			if line[j] == ".":
				field[i][j] = 0

	pq = []

	for i in range(n):
		for j in range(m):
			if field[i][j] == 0 and not visited[i][j]:
				heapq.heappush(pq, -search(i, j))

	cnt = 0
	
	while h > 0:
		h += heapq.heappop(pq)
		cnt += 1
	
	print(cnt)
