from collections import deque

class Lineseg:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.start = -1e18
	
	def __str__(self):
		return f"y={self.a}x+{self.b}, from {self.start}"
	
	def intersect(self, other):
		assert self.a!=other.a
		return (other.b-self.b)/(self.a-other.a)
	
	def putx(self, x):
		return self.a*x+self.b

n=int(input())

a,b,c=map(int,input().split())
L=list(map(int,input().split()))
pfsum = [0]
for i in L:pfsum.append(pfsum[-1]+i)

dp=[0]*n

lines = deque()
idx = 0
dp[0] = a*L[0]**2+b*L[0]+c
for i in range(1, n):
	B = pfsum[i]
	C = a*pfsum[i]**2 - b*pfsum[i] + dp[i-1]
	# print(B, C)
	next_line = Lineseg(B, C)
	#line을 추가. 이전 line들이 덮힌다면 그렇게 되지 않을 때까지 pop.
	# print(next_line)
	x=0
	while lines:
		x = next_line.intersect(lines[-1])
		if lines[-1].start < x:break
		lines.pop()
	next_line.start = x
	lines.append(next_line)
	# for l in lines:print(l, end=' ')
	# print(lines[0])
	
	#이분 탐색으로 A[i]일 때의 line을 구함
	now = -2*a*pfsum[i+1]
	D = a*pfsum[i+1]**2+b*pfsum[i+1]+c
	while idx < len(lines)-1 and lines[idx+1].start < now:
		idx+=1
	dp[i] = max(lines[idx].putx(now)+D, a*pfsum[i+1]**2+b*pfsum[i+1]+c)
	# if lines[-1].start > now:
	# 	l=0
	# 	h=len(lines)-1
	# 	while h-1>l:
	# 		mid = (l+h)//2
	# 		if lines[mid].start > now:h=mid
	# 		else:l=mid
	# 	dp[i] = lines[l].putx(now)+D
	# else:
	# 	dp[i] = lines[-1].putx(now)+D
	# print(dp)
print(dp[-1])