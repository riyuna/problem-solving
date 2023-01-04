import sys
from math import gcd
input=sys.stdin.readline

MAX = 4000100
tree = [0] * MAX  
lazy = [0] * MAX 

def updateRangeUtil(si, ss, se, us, ue, diff) : 
	if (lazy[si] != 0) : 
		tree[si] += (se - ss + 1) * lazy[si]
		if (ss != se) : 
			lazy[si * 2 + 1] += lazy[si]
			lazy[si * 2 + 2] += lazy[si]
		lazy[si] = 0
	if (ss > se or ss > ue or se < us) : 
		return
	if (ss >= us and se <= ue) : 
		tree[si] += (se - ss + 1) * diff
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
		tree[si] += (se - ss + 1) * lazy[si]
		if (ss != se) : 
			lazy[si * 2 + 1] += lazy[si]
			lazy[si * 2 + 2] += lazy[si]
		lazy[si] = 0
	if (ss > se or ss > qe or se < qs) : 
		return 0
	if (ss >= qs and se <= qe) : 
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

class sgTree:
    def __init__(self,L):
        self.len=len(L)
        self.tree=[0]*self.len+L
        for i in range(self.len-1, 0, -1):
            self.tree[i]=gcd(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, val):
        i+=(self.len-1)
        self.tree[i]=val
        while i>1:
            i//=2
            self.tree[i]=gcd(self.tree[2*i],self.tree[2*i+1])

    def res(self, l, r):
        l+=(self.len-1)
        r+=(self.len-1)
        tot=0
        while l<=r:
            if l%2:
                tot=gcd(tot, self.tree[l])
                l+=1
            l//=2
            if not r%2:
                tot=gcd(tot, self.tree[r])
                r-=1
            r//=2
        return tot

n=int(input())
L=list(map(int,input().split()))
constructST(L, n)
diff=[]
for i in range(n-1):
	diff.append(abs(L[i+1]-L[i]))
gcdseg=sgTree(diff)

for i in ' '*int(input()):
	t,a,b=map(int,input().split())

	if t!=0:
		updateRange(n, a-1, b-1, t)
		if a!=1:
			gcdseg.update(a-1, abs(getSum(n, a-1, a-1)-getSum(n, a-2, a-2)))
		if b!=n:
			gcdseg.update(b, abs(getSum(n, b, b)-getSum(n, b-1, b-1)))
	else:
		if a==b:print(getSum(n, a-1, a-1))
		else:
			print(gcd(getSum(n, a-1, a-1), gcdseg.res(a, b-1)))
	