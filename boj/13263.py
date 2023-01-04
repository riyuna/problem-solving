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
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[0]*n

lines = deque()

for i in range(1, n):
	next_line = Lineseg(B[i-1], dp[i-1])
	#line을 추가. 이전 line들이 덮힌다면 그렇게 되지 않을 때까지 pop.
	x=0
	while lines:
		x = next_line.intersect(lines[-1])
		if lines[-1].start < x:break
		lines.pop()
	next_line.start = x
	lines.append(next_line)
	# print(lines[0])
	
	#이분 탐색으로 A[i]일 때의 line을 구함
	now = A[i]
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
print(dp[-1])