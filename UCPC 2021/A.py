MAX = 1000010
tree_lazy = [[-1, 0, 0, 0, 0] for i in range(MAX)]
lazy = [[-1, 0, 0, 0, 0] for i in range(MAX)]
import sys
input=sys.stdin.readline

def node_maker(n):
    if n not in (0,9):
        return [n, 0, 0, 0, 0]
    if n==0:
        return [n, 0, 0, 1, 1]
    if n==9:
        return [n, 1, 1, 0, 0]

def combine(L1, L2):
    if (L1[0], L2[0]) in [(9, 9), (-1, 9), (9, -1)]:res=9
    elif (L1[0], L2[0]) in [(0, -1), (-1, 0), (0, 0)]:res=0
    else:res=1
    return [
        res,
        L1[1] if L1[0]!= 9 else L1[1]+L2[1],
        L2[2] if L2[0]!= 9 else L1[2]+L2[2],
        L1[3] if L1[0]!= 0 else L1[3]+L2[3],
        L1[4] if L2[0]!= 0 else L1[4]+L2[4],
    ]

def updateRangeUtil(si, ss, se, us, ue, diff) : 
	if (lazy[si][0] != -1) : 
		tree_lazy[si][0] = lazy[si][0]
		if (ss != se) : 
			lazy[si * 2 + 1] = combine(lazy[si * 2 + 1], lazy[si])
			lazy[si * 2 + 2] = combine(lazy[si * 2 + 1], lazy[si])
		lazy[si] = [-1, 0, 0, 0, 0]
	if (ss > se or ss > ue or se < us) : 
		return
	if (ss >= us and se <= ue) : 
		tree_lazy[si][0] = diff
		if (ss != se) : 
			lazy[si * 2 + 1] = combine(lazy[si * 2 + 1], node_maker(diff))
			lazy[si * 2 + 2] = combine(lazy[si * 2 + 2], node_maker(diff))
		return
	mid = (ss + se) // 2
	updateRangeUtil(si * 2 + 1, ss, 
					mid, us, ue, diff)
	updateRangeUtil(si * 2 + 2, mid + 1, 
					se, us, ue, diff)
	tree_lazy[si] = combine(tree_lazy[si * 2 + 1], tree_lazy[si * 2 + 2])
    
def updateRange(n, us, ue, diff) : 
	updateRangeUtil(0, 0, n - 1, us, ue, diff)

def getSumUtil(ss, se, qs, qe, si) : 
	if (lazy[si] != 0) : 
		tree_lazy[si] += (se - ss + 1) * lazy[si]
		if (ss != se) : 
			lazy[si * 2 + 1] += lazy[si]
			lazy[si * 2 + 2] += lazy[si]
		lazy[si] = 0
	if (ss > se or ss > qe or se < qs) : 
		return 0
	if (ss >= qs and se <= qe) : 
		return tree_lazy[si]
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
		tree_lazy[si][0] = arr[ss]
		return
	mid = (ss + se) // 2
	constructSTUtil(arr, ss, mid, si * 2 + 1)
	constructSTUtil(arr, mid + 1, se, si * 2 + 2)
	tree_lazy[si] = tree_lazy[si * 2 + 1] + tree_lazy[si * 2 + 2] 
    
def constructST(arr, n) : 
	constructSTUtil(arr, 0, n - 1, 0)
    
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
L=[]
for i in ' '*n:L.append(int(input()))
constructST(L, n)
for i in ' '*(m+k):
    M=list(map(int,input().split()))
    if M[0]==1:updateRange(n,M[1]-1,M[2]-1,M[3])
    else:print(getSum(n,M[1]-1,M[2]-1))