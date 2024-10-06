import sys
input=sys.stdin.readline

for i in ' '*int(input()):
	n=int(input())
	L=[]
	for j in range(1, n**2+1):
		if j%2:L.append((j+1)//2)
		else:L.append(n**2-j//2+1)
	for j in range(n):
		part = L[j*n:j*n+n]
		if j%2:part = part[::-1]
		for k in part:
			print(k,end=' ')
		print()