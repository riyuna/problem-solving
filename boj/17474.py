MAX = 4000100
tree = [[0, 0, 0, 0] for i in range(MAX)]  
lazy = [0] * MAX 

def break_condition(ss, se, us, ue):
	return ss > se or ss > ue or se < us

def tag_condition(ss, se, us, ue):
	return ss >= us and se <= ue

def updateRangeUtil(si, ss, se, us, ue, diff) : 
	if (lazy[si] != 0) : 
		tree[si] += lazy[si]*((se-ss+1)%2)
		if (ss != se) : 
			lazy[si * 2 + 1] += lazy[si]
			lazy[si * 2 + 2] += lazy[si]
		lazy[si] = 0
	if break_condition(ss, se, us, ue) : 
		return
	if tag_condition(ss, se, us, ue): 
		tree[si] += diff*((se-ss+1)%2)
		if (ss != se) : 
			lazy[si * 2 + 1] += diff
			lazy[si * 2 + 2] += diff
		return
	mid = (ss + se) // 2
	updateRangeUtil(si * 2 + 1, ss, 
					mid, us, ue, diff)
	updateRangeUtil(si * 2 + 2, mid + 1, 
					se, us, ue, diff)
	tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2]
    
def updateRange(n, us, ue, diff) : 
	updateRangeUtil(0, 0, n - 1, us, ue, diff)

def getSumUtil(ss, se, qs, qe, si) : 
	if (lazy[si] != 0) : 
		tree[si] += lazy[si]*((se-ss+1)%2)
		if (ss != se) : 
			lazy[si * 2 + 1] += lazy[si]
			lazy[si * 2 + 2] += lazy[si]
		lazy[si] = 0
	if break_condition(ss, se, qs, qe) : 
		return 0
	if tag_condition(ss, se, qs, qe) : 
		return tree[si]
	mid = (ss + se) // 2
	return (getSumUtil(ss, mid, qs, qe, 2 * si + 1) +
			getSumUtil(mid + 1, se, qs, qe, 2 * si + 2))

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
	tree[si] = tree[si * 2 + 1] + tree[si * 2 + 2] 
    
def constructST(arr, n) : 
	constructSTUtil(arr, 0, n - 1, 0)
    
import sys
input=sys.stdin.readline
n=int(input())
L=list(map(int,input().split()))
constructST(L, n)
for i in ' '*(int(input())):
	M=list(map(int,input().split()))
	if M[0]==1:updateRange(n,M[1],M[2],M[3])
	else:print(getSum(n,M[1],M[2]))
