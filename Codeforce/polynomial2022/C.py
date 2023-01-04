import sys
input=sys.stdin.readline
for _ in ' '*int(input()):
	n=int(input())
	s=input().strip()
	mem=-1
	for i in range(n-1):
		if i==0:
			mem=1
			print(1, end=' ')
			continue
		if s[i-1]==s[i]:
			print(mem,end=' ')
		else:
			mem=i+1
			print(mem,end=' ')
	print()