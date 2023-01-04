from collections import deque

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

n=int(input())
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))
L.sort()
newL=deque()
for w, h in L:
	while newL and newL[-1][1]<=h: newL.pop()
	newL.append([w,h])
L=newL
n=len(L)
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
dp=[0]*n
dp[0] = L[0][0]*L[0][1]
lines = deque()

for i in range(1, n):
	next_line = Lineseg(L[i][1], dp[i-1])
	#line을 추가. 이전 line들이 덮힌다면 그렇게 되지 않을 때까지 pop.
	x=0
	while lines:
		x = next_line.intersect(lines[-1])
		if lines[-1].start < x:break
		lines.pop()
	next_line.start = x
	lines.append(next_line)
	
	#이분 탐색으로 A[i]일 때의 line을 구함
	now = L[i][0]
	if lines[-1].start > now:
		l=0
		h=len(lines)-1
		while h-1>l:
			mid = (l+h)//2
			if lines[mid].start > now:h=mid
			else:l=mid
		dp[i] = lines[l].putx(now)
	else:
		dp[i] = lines[-1].putx(now)
	dp[i] = min(dp[i], L[0][1]*L[i][0])
print(dp[-1])