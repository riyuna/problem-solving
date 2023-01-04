import sys
input=sys.stdin.readline

for i in ' '*int(input()):
	n=int(input())
	s=input().strip()
	one = False
	for j in range(n):
		if s[j]=='1' and not one:
			one=True
			if j:print('+',end='')
		elif s[j]=='1' and one:
			one=False
			print('-',end='')
		else:
			if j:print('+',end='')
	print()