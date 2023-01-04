n,m=map(int,input().split())
q=int((n*m)**0.5)
if n>=m and q**2 == n*m:
	print(n*q)
	for i in range(n):
		for j in range(i*q, i*q+q):
			print(i%n+1, j%n+1)

else:
	print(-1)