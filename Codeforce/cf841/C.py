import sys
input=sys.stdin.readline
sqs = []
for i in range(520):sqs.append(i**2)
def solve(L):
	p=0
	d=dict()
	d[0]=1
	res=0
	for i in range(len(L)):
		p^=L[i]
		for j in sqs:
			k=p^j
			if k in d:res-=d[k]
		res+=(i+1)
		if p not in d:d[p]=0
		d[p]+=1
	return res

for i in ' '*int(input()):
	n=int(input())
	L=list(map(int,input().split()))
	print(solve(L))