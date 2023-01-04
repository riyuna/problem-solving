import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n=int(input())
L=[]
for i in ' '*n:L.append(int(input()))
M=[]
for i in ' '*int(input()):M.append(int(input()))

M.sort()

dp = dict()

def solve(a, b1, b2, state=True):
	if a==n and b1==b2:
		return 0
	if (a,b1,b2,state) in dp:
		return dp[(a,b1,b2,state)]
	
	if a==n and state:
		res = max(solve(a, b1, b2-1, False)+M[b2-1], solve(a,b1+1,b2,True))
	
	elif a==n and not state:
		res = solve(a, b1+1, b2, True)
	
	elif b1==b2 and state:
		res = max(solve(a+1,b1,b2,False)+L[a], solve(a+1,b1,b2,True))
	
	elif b1==b2 and not state:
		res = solve(a+1, b1, b2, 1)
	
	else:
		perm = 0
		if state:
			perm = max(perm, max(solve(a+1,b1,b2,False)+L[a], solve(a,b1,b2-1,False)+M[b2-1]))
		
		perm = max(perm, max(solve(a+1,b1,b2,True), solve(a,b1+1,b2,True)))
		res = perm
	
	dp[(a,b1,b2,state)] = res
	return res

print(solve(0,0,len(M),True))