import sys
input=sys.stdin.readline
def solve(n1, m1, n2, m2):
	res=0
	k=1
	for i in range(n2+1):
		k*=(n1-m1+1+i)
		k/=(n1+2+i)
	res+=k
	for i in range(m2):
		k*=(m1+1+i)
		k*=(n2+1-i)
		k/=(i+1)
		k/=(n1+n2-m1+1-i)
		res+=k
	return res

for i in ' '*int(input()):
    n1,m1,n2,m2=map(int,input().split())
    print(solve(n1,m1,n2,m2))