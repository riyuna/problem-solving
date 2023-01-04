import sys
input = sys.stdin.readline
n=int(input())
dp = [[[[0]*11 for i in range(11)]for i in range(11)]for i in range(11)]
L=[]
for i in ' '*n:
	a,b,c,d=list(input().strip())
	for j in range(2):
		for k in range(2):
			for s in range(2):
				for t in range(2):
					dp[int(a) if j else 10][int(b) if k else 10][int(c) if s else 10][int(d) if t else 10]+=1
	L.append(int(a+b+c+d))

res = 0

def solve(mem, a, b, c, d, sign):
	global res

	for t in range(2**len(mem)):
		nmem = []
		for r in range(len(mem)):
			if t%2:nmem.append(mem[r])
			t//=2
		sign = (-1)**(len(mem)-len(nmem))
		aa = [10] if 1 in nmem else a
		bb = [10] if 2 in nmem else b
		cc = [10] if 3 in nmem else c
		dd = [10] if 4 in nmem else d

		for i in range(2):
			for j in range(2):
				for k in range(2):
					for s in range(2):
						try:
							res += sign*dp[aa[i]][bb[j]][cc[k]][dd[s]]
						except:
							continue

for i in range(n):
	for j in range(i):
		x, y = L[i], L[j]
		a1, b1, c1, d1 = map(int, list(str(x)))
		a2, b2, c2, d2 = map(int, list(str(y)))
		a0, b0, c0, d0 = a1!=a2, b1!=b2, c1!=c2, d1!=d2

		mem = []
		if a0:mem.append(1)
		if b0:mem.append(2)
		if c0:mem.append(3)
		if d0:mem.append(4)
		aa = [a1] if not a0 else [a1, a2]
		bb = [b1] if not b0 else [b1, b2]
		cc = [c1] if not c0 else [c1, c2]
		dd = [d1] if not d0 else [d1, d2]

		solve(mem, aa, bb, cc, dd, 1)

print(res//3)