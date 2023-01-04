from collections import deque
import sys
input=sys.stdin.readline
print=sys.stdout.writelines

class Lineseg:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.start = 0
	
	def __str__(self):
		return f"y={self.a}x+{self.b}, from {self.start}"
	
	def intersect(self, other):
		assert self.a!=other.a
		return (other.b-self.b)/(self.a-other.a)
	
	def putx(self, x):
		return self.a*x+self.b
	
class Node:
	def __init__(self, line=Lineseg, s=int, e=int, l=-1, r=-1):
		self.start = s
		self.end = e
		self.line = line
		self.left = l
		self.right = r
	
	def __str__(self):
		return f"Line: {str(self.line)}, s,e,l,r={self.start}, {self.end}, {self.left}, {self.right}"

class LCtree:
	def __init__(self, s=-1e18, e=1e18):
		self.tree = [Node(Lineseg(0, -1e18),s, e)]
		#최솟값이라 1e18. 최대면 반대로
	
	def __str__(self):return str(self.tree)
	
	def update(self, node, l=Lineseg):
		s = self.tree[node].start
		e = self.tree[node].end
		mid = (s+e)//2

		under = self.tree[node].line
		over = l
		if under.putx(s)>over.putx(s):
			under,over = over,under
		#시작점에 따라서 under와 over를 결정
		#지금은 최솟값을 구하는 거라 under over를 정반대로 함

		if under.putx(e) <= over.putx(e):
			self.tree[node].line = over
			return
			#만약 모든 구간에서 over가 위에 있으면, 그냥 바꿔치기
			#이것도 최솟값이라 under over 부등호 방향 반대.
		if under.putx(mid) <= over.putx(mid):
			self.tree[node].line = over
			if self.tree[node].right == -1:
				self.tree[node].right = len(self.tree)
				self.tree.append(Node(Lineseg(0, -1e18), mid+1, e))
			self.update(self.tree[node].right, under)
		
		else:
			self.tree[node].line = under
			if self.tree[node].left == -1:
				self.tree[node].left = len(self.tree)
				self.tree.append(Node(Lineseg(0, -1e18), s, mid))
			self.update(self.tree[node].left, over)
	
	def value(self, node, x):
		if node == -1:return -1e18
		#최대면 -1e18
		s = self.tree[node].start
		e = self.tree[node].end

		mid = (s+e)//2
		if x<=mid:
			return max(self.tree[node].line.putx(x), self.value(self.tree[node].left, x))
		else:
			return max(self.tree[node].line.putx(x), self.value(self.tree[node].right, x))
		#최솟값이라 min, 최대면 max
lines = LCtree()

n=int(input())
for i in ' '*n:
	L=list(map(int,input().split()))
	if len(L)==3:
		next_line = Lineseg(L[1], L[2])
		lines.update(0, next_line)
	
	else:
		x = L[1]
		print(str(lines.value(0, x))+'\n')