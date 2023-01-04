n=int(input())
L=list(map(int,input().split()))

def solve(L):
	res=0
	ct=0
	for i in range(len(L)):
		ct+=L[i]
		res=max(res, ct/(i+1))
	return res

print(max(solve(L), solve(L[::-1])))