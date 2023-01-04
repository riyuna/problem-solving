r,c=map(int,input().split())
L=[]
for i in ' '*r:L.append(list(map(int,input().split())))

def solve(L):
	res=[]
	if len(L)%2:
		for i in range(len(L)):
			for j in range(len(L[0])-1):
				if i%2:res.append('L')
				else:res.append('R')
			if i!=len(L)-1:res.append('D')
		return res
	if len(L[0])%2:
		for i in range(len(L[0])):
			for j in range(len(L)-1):
				if i%2:res.append('U')
				else:res.append('D')
			if i!=len(L[0])-1:res.append('R')
		return res
	
	mem = (-1, -1)
	mn = 10000
	for i in range(len(L)):
		for j in range(len(L[0])):
			if (i+j)%2 and L[i][j]<mn:
				mem=(i,j)
				mn=L[i][j]
	
	bd = mem[0]
	if bd%2:bd-=1
	for i in range(bd):
		for j in range(len(L[0])-1):
			if i%2:res.append('L')
			else:res.append('R')
		res.append('D')
	
	for i in range(mem[1]):
		if i%2:res.append('U')
		else:res.append('D')
		res.append('R')

	for i in range(mem[1], len(L[0])-1):
		res.append('R')
		if i%2:res.append('U')
		else:res.append('D')
	
	remain = len(L)-bd-2

	for i in range(remain):
		res.append('D')
		for j in range(len(L[0])-1):
			if i%2:res.append('R')
			else:res.append('L')
	
	return res

for i in solve(L):print(i,end='')