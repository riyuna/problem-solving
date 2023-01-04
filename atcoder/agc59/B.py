import sys
input = sys.stdin.readline

for _ in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	ct=dict()
	for i in L:
		if i not in ct:ct[i]=0
		ct[i]+=1
	ctL=list(ct.items())
	ctL.sort(key = lambda i:i[1], reverse=True)
	res = ['' for i in range(n)]

	watching = 0
	cte = 0
	cto = 0
	even=True
	odd=False
	while watching < len(ctL):
		for i in range(ctL[watching][1]):
			try:
				if even:
					res[cte*2] = str(ctL[watching][0])
					cte+=1
				else:
					res[cto*2+1] = str(ctL[watching][0])
					cto+=1
			except:
				if even:
					even=False
					odd = True
					res[cto*2+1] = str(ctL[watching][0])
					cto+=1
				else:
					even=True
					odd=False
					res[cte*2] = str(ctL[watching][0])
					cte+=1
		watching+=1
		even = (cte<=cto)
		odd = not even
	
	print(' '.join(res))