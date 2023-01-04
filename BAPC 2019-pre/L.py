import sys

input = sys.stdin.readline


if __name__ == "__main__":
	n = int(input())

	points = [list(map(int, input().split())) for _ in range(n)]
	points.sort()

	print(points)

	if n%2:
		x, y = points[n//2]
		print(x - 10**17, y - 1)
		print(x + 10**17, y + 1)
	else:
		x, y = points[n//2]
		print(x - 10**17, y - 1)
		print(x + 10**17, y + 2)
