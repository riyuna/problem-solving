n,m=map(int,input().split())

L=list(map(int,input().split()))

mem = []

b = list(range(1, n+1))

for i in L:
	b[i-1], b[i] = b[i], b[i-1]
	mem.append((b[i-1], b[i]))

rev = dict()
for i in range(n):
	rev[b[i]] = i

for i in range(m):
	t1, t2 = mem[i]
	if t1 == 1:
		print(rev[t2]+1)
	elif t2==1:
		print(rev[t1]+1)
	else:print(rev[1]+1)