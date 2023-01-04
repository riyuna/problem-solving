import sys


input = sys.stdin.readline


if __name__ == "__main__":
	h, w = map(int, input().split())

	rx_sum = 0
	x_sum = 0

	for _ in range(h):
		line = input().rstrip()

		for i in range(w):
			if line[i] != ".":
				rx_sum += i
				x_sum += 1
	
	for i in range(w):
		if line[i] != ".":
			left = i
			break
	
	for i in range(w-1, -1, -1):
		if line[i] != ".":
			right = i
			break
	
	if rx_sum < (left-0.5) * x_sum:
		print("left")
	elif rx_sum > (right+0.5) * x_sum:
		print("right")
	else:
		print("balanced")
