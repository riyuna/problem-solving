n=int(input())
if n%4 not in (0, 1):print('No')
else:
	print('Yes')
	res = []
	if n%4 == 0:
		if n == 4:res = [1, 2, 1, 3, 2 ,0, 0, 3]
		elif n == 8:res = [7, 5, 3, 1, 6, 1, 3, 5, 7, 2, 4, 6, 2, 0, 0, 4]
		else:
			for i in range(n//2):
				res.append(n-i*2-1)
			res.append(n-2)
			for i in range(n//2):
				res.append(i*2+1)
			
			res.append(n//2-2)
			for i in range(n//2-2):
				if i==n//4-1:continue
				res.append(n-2*i-4)
			res.append(n-2)
			res.append(n//2-2)
			for i in range(n//2-2):
				if i*4+8 == n:
					res.append(0)
					res.append(0)
					continue
				res.append(i*2+2)
	else:
		if n==1: res = [0, 0]
		elif n==5: res = [4, 1, 3, 1, 2, 4, 3, 2, 0, 0]
		else:
			for i in range(n//2):
				res.append(n-i*2-1)
			res.append(n//2+1)
			res.append(n-2)
			for i in range(n//2):
				res.append(i*2+2)
			res.append(n//2+1)
			for i in range(n-4, -1, -2):
				if i!=n//2+1:res.append(i)
			res.append(n-2)
			for i in range(1, n-2, 2):
				if i==n//2+1:
					res.append(0)
					res.append(0)
					continue
				res.append(i)
	for i in res:print(i,end=' ')