from collections import deque

class Lineseg:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.start = 1e18
	
	def __str__(self):
		return f"y={self.a}x+{self.b}, until {self.start}"
	
	def intersect(self, other):
		assert self.a!=other.a
		return (other.b-self.b)/(self.a-other.a)
	
	def putx(self, x):
		return self.a*x+self.b

n=int(input())
L=list(map(int,input().split()))
def solve(L):
	pfsum = [0]
	for i in L:pfsum.append(pfsum[-1]+i)

	dp=[0]*n

	lines = deque()
	dp[0] = pfsum[-1]
	for i in range(1, n):
		B = -i+1
		C = pfsum[i-1]
		# print(B, C)
		next_line = Lineseg(B, C)
		#line을 추가. 이전 line들이 덮힌다면 그렇게 되지 않을 때까지 pop.
		# print(next_line)
		x=0
		while lines:
			x = next_line.intersect(lines[0])
			if lines[0].start > x:break
			lines.popleft()
		if i>1:next_line.start = x
		lines.appendleft(next_line)
		
		#이분 탐색으로 A[i]일 때의 line을 구함
		now = L[i]
		D = (i+1)*L[i]+pfsum[-1]-pfsum[i+1]
		# while idx < len(lines)-1 and lines[idx].start < now:
		# 	idx+=1
		# if idx>=len(lines)-1:idx=len(lines)-1
		# dp[i] = lines[idx].putx(now)+D
		if lines[0].start < now:
			l=0
			h=len(lines)-1
			while h-1>l:
				mid = (l+h)//2
				if lines[mid].start > now:h=mid
				else:l=mid
			dp[i] = lines[h].putx(now)+D
		else:
			dp[i] = lines[0].putx(now)+D
	return(max(dp[1:]))

print(solve(L))
print(solve(L[::-1]))