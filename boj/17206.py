def sumto(n, k):
	return n*(n+1)//2*k
def solve(n):
	a=n//3
	b=n//7
	c=n//21
	return sumto(a,3)+sumto(b,7)-sumto(c,21)

n=int(input())
for i in map(int,input().split()):
	print(solve(i))