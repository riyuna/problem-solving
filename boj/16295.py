import sys


input = sys.stdin.readline


if __name__ == "__main__":
	n, m = map(int, input().split())

	sockets = list(map(int, input().split()))
	wires = list(map(int, input().split()))

	p = 0
	poss = True
	done = False

	for d in range(1, n-1):
		put = False
		
		vals = []
		for i in range(0, n-d):
			vals.append(sockets[i+d] - sockets[i])
		vals.sort()

		for i in range(len(vals)):
			if wires[p] >= vals[i]:
				p += 1
				put = True
				if p == m:
					done = True
					break
			else:
				break
		
		if not put:
			break
	
	if done:
		print("yes")
	else:
		print("no")
