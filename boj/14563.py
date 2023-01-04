n=int(input())
def solve(n):
	ct=0
	for i in range(1,n):
		if n%i==0:ct+=i
	if ct==n:return 'Perfect'
	elif ct<n:return 'Deficient'
	return 'Abundant'

for i in map(int,input().split()):
	print(solve(i))