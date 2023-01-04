import sys
input=sys.stdin.readline

INF = 1e18
node = []

# class Lineseg:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b
# 		self.start = 0
	
# 	def __str__(self):
# 		return f"y={self.a}x+{self.b}, from {self.start}"
	
# 	def intersect(self, other):
# 		assert self.a!=other.a
# 		return (other.b-self.b)/(self.a-other.a)
	
# 	def putx(self, x):
# 		return self.a*x+self.b

#Li-Chao with no class
def putx(line,x):
	a,b=line
	return a*x+b
def init(st, ed):
	node.append([-1, -1, st, ed, [0,-INF]])

def update(x, line):
	s,e,l,r,lo=node[x]
	m=(l+r)//2

	hi=line
	if putx(lo, l)>putx(hi,l):
		lo,hi=hi,lo
	if putx(lo, r)<=putx(hi,r):
		node[x][-1]=hi
		return
	
	if putx(lo,m) < putx(hi,m):
		node[x][-1]=hi
		if e==-1:
			node[x][1]=len(node)
			node.append([-1, -1, m+1, r, [0,-INF]])
		update(node[x][1], lo)
		return
	
	else:
		node[x][-1]=lo
		if s==-1:
			node[x][0]=len(node)
			node.append([-1,-1,l,m,[0,-INF]])
		update(node[x][0],hi)
		return
	
def value(k,x):
	if k==-1:return -INF
	a,b,l,r,ln=node[k]
	m=(l+r)//2
	
	if x<m:return max(putx(ln,x), value(a,x))
	else:return max(putx(ln,x),value(b,x))

init(-1e12, 1e12)
n=int(input())
while n:
	n-=1
	L=list(map(int,input().split()))
	if len(L)==3:
		update(0, L[1:])
	
	else:
		print((value(0, L[1])))