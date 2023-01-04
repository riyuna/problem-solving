import random
MAX = 4000100
tree = [0] * MAX  
lazy = [[1, 0] for i in range(MAX)] 
mod = 1000000007

def updateRangeUtil(si, ss, se, us, ue, mul, sum) : 
	if (lazy[si] != [1, 0]) : 
		tree[si] *= lazy[si][0]
		tree[si] += lazy[si][1]*(se-ss+1)
		tree[si]%=mod
		if (ss != se) : 
			lazy[si*2+1][0] *= lazy[si][0]
			lazy[si*2+1][0] %= mod
			lazy[si*2+1][1] *= lazy[si][0]
			lazy[si*2+1][1] += lazy[si][1]
			lazy[si*2+1][1] %= mod

			lazy[si*2+2][0] *= lazy[si][0]
			lazy[si*2+2][0] %= mod
			lazy[si*2+2][1] *= lazy[si][0]
			lazy[si*2+2][1] += lazy[si][1]
			lazy[si*2+2][1] %= mod
		lazy[si] = [1, 0]
	if (ss > se or ss > ue or se < us) : 
		return
	if (ss >= us and se <= ue) : 
		tree[si] *= mul
		tree[si] += sum*(se-ss+1)
		tree[si] %= mod

		if (ss != se) : 
			lazy[si*2+1][0] *= mul
			lazy[si*2+1][0] %= mod
			lazy[si*2+1][1] *= mul
			lazy[si*2+1][1] += sum
			lazy[si*2+1][1] %= mod

			lazy[si*2+2][0] *= mul
			lazy[si*2+2][0] %= mod
			lazy[si*2+2][1] *= mul
			lazy[si*2+2][1] += sum
			lazy[si*2+2][1] %= mod
		return

	mid = (ss + se) // 2
	updateRangeUtil(si * 2 + 1, ss, 
					mid, us, ue, mul, sum)
	updateRangeUtil(si * 2 + 2, mid + 1, 
					se, us, ue, mul, sum)
	tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]
	tree[si] %= mod
    
def updateRange(n, us, ue, mul, sum) : 
	updateRangeUtil(0, 0, n - 1, us, ue, mul, sum)

def getSumUtil(ss, se, qs, qe, si) : 
	if (lazy[si] != [1, 0]) : 
		tree[si] *= lazy[si][0]
		tree[si] += lazy[si][1]*((se-ss+1))
		tree[si] %= mod
		if (ss != se) : 
			lazy[si*2+1][0] *= lazy[si][0]
			lazy[si*2+1][1] *= lazy[si][0]
			lazy[si*2+2][0] *= lazy[si][0]
			lazy[si*2+2][1] *= lazy[si][0]
			
			lazy[si*2+1][1] += lazy[si][1]
			lazy[si*2+2][1] += lazy[si][1]
		lazy[si] = [1, 0]
	if (ss > se or ss > qe or se < qs) : 
		return 0
	if (ss >= qs and se <= qe) : 
		return tree[si]%mod
	mid = (ss + se) // 2
	return ((getSumUtil(ss, mid, qs, qe, 2 * si + 1) +
			getSumUtil(mid + 1, se, qs, qe, 2 * si + 2))%mod)

def getSum(n, qs, qe) : 
	if (qs < 0 or qe > n - 1 or qs > qe) : 
		print("Invalid Input")
		return -1
	return getSumUtil(0, n - 1, qs, qe, 0)

def constructSTUtil(arr, ss, se, si) : 
	if (ss > se) : 
		return 
	if (ss == se) : 
		tree[si] = arr[ss]
		return
	mid = (ss + se) // 2
	constructSTUtil(arr, ss, mid, si * 2 + 1)
	constructSTUtil(arr, mid + 1, se, si * 2 + 2)
	tree[si] = (tree[si * 2 + 1] + tree[si * 2 + 2])%mod
    
def constructST(arr, n) : 
	constructSTUtil(arr, 0, n - 1, 0)
    
import sys
input=sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))

constructST(L, n)
for i in ' '*(int(input())):
	M=list(map(int,input().split()))
	if M[0]==4:
		print(getSum(n, M[1]-1, M[2]-1)%mod)
	else:
		q,x,y,v=M
		if q==1: updateRange(n, x-1, y-1, 1, v)
		elif q==2: updateRange(n, x-1, y-1, v, 0)
		else:
			updateRange(n, x-1, y-1, 0, v)