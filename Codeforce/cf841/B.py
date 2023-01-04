import sys
input=sys.stdin.readline

for i in ' '*int(input()):
	n=int(input())
	res = n*(n+1)*(2*n+1)//3 - n*(n+1)//2
	res*=2022
	print(res%1000000007)